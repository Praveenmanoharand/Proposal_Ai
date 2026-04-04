// ================================
// STATE
// ================================
const state = {
    currentProposal: null,
    isGenerating: false,
    userPlan: 'free',       // Will be fetched from /api/user-status
    planLimits: {},
    usedThisMonth: 0,
    totalProposals: 0,      // Total proposals ever (for feedback check)
    feedbackGiven: false,   // Has user already given feedback?
    sidebarOpen: false,
    isEditing: false
};

// ================================
// DOM ELEMENTS
// ================================
const elements = {
    form: document.getElementById('proposalForm'),
    generateBtn: document.getElementById('generateBtn'),
    loadingOverlay: document.getElementById('loadingOverlay'),
    emptyState: document.getElementById('emptyState'),
    proposalDocument: document.getElementById('proposalDocument'),
    previewFooter: document.getElementById('previewFooter'),
    statusDot: document.getElementById('statusDot'),
    statusText: document.getElementById('statusText'),
    copyBtn: document.getElementById('copyBtn'),
    downloadBtn: document.getElementById('downloadBtn'),
    sendBtn: document.getElementById('sendBtn'),
    editBtn: document.getElementById('editBtn'),
    toastContainer: document.getElementById('toastContainer'),
    nav: document.querySelector('.nav-container'),
    predictPrice: document.getElementById('predictPrice'),
    projectPrice: document.getElementById('projectPrice'),
    increaseBtn: document.getElementById('increaseBtn'),
    decreaseBtn: document.getElementById('decreaseBtn'),
    // Sidebar Elements
    sidebar: document.getElementById('sidebar'),
    sidebarOverlay: document.getElementById('sidebarOverlay'),
    sidebarToggleBtn: document.getElementById('sidebarToggleBtn'),
    closeSidebar: document.getElementById('closeSidebar'),
    historyList: document.getElementById('historyList'),
    newProposalBtn: document.getElementById('newProposalBtn'),
    toggleHistoryBtn: document.getElementById('toggleHistoryBtn'),
    // Feedback Elements
    feedbackModal: document.getElementById('feedbackModal'),
    feedbackModalOverlay: document.getElementById('feedbackModalOverlay'),
    feedbackForm: document.getElementById('feedbackForm'),
    closeFeedbackModal: document.getElementById('closeFeedbackModal'),
    feedbackContainer: document.getElementById('feedbackContainer'),
    // Mobile Nav
    hamburgerBtn: document.getElementById('hamburgerBtn'),
    mobileNav: document.getElementById('mobileNav'),
    mobilePlanBadge: document.getElementById('mobilePlanBadge')
};

// ================================
// NAVIGATION SCROLL
// ================================
window.addEventListener('scroll', () => {
    if (elements.nav) {
        elements.nav.classList.toggle('scrolled', window.pageYOffset > 50);
    }
}, { passive: true });

// ================================
// TOAST NOTIFICATIONS
// ================================
function showToast(message, type = 'success') {
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;

    const icons = {
        success: `<svg class="toast-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#00d4aa" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>`,
        error:   `<svg class="toast-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#ef4444" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/></svg>`,
        upgrade: `<svg class="toast-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>`
    };

    toast.innerHTML = `${icons[type] || icons.success}<span class="toast-message">${message}</span>`;
    if (type === 'upgrade') {
        toast.style.borderColor = 'rgba(245,158,11,0.3)';
        const upgradeLink = document.createElement('a');
        upgradeLink.href = '#pricing';
        upgradeLink.textContent = 'Upgrade →';
        upgradeLink.style.cssText = 'color:#f59e0b;font-weight:700;font-size:0.8rem;margin-left:10px;text-decoration:none;white-space:nowrap;';
        toast.appendChild(upgradeLink);
    }
    elements.toastContainer.appendChild(toast);

    setTimeout(() => {
        toast.style.animation = 'toastIn 0.3s ease-out reverse';
        setTimeout(() => toast.remove(), 300);
    }, 5000);
}

// ================================
// UPDATE UI FOR PLAN
// ================================
function updateUIForPlan() {
    // Update usage indicator
    const limit = state.planLimits?.proposals_per_month || null;
    const used = state.usedThisMonth || 0;
    const remaining = limit ? limit - used : null;
    updateUsageIndicator(remaining, limit);

    // Update sidebar user plan display
    renderSubscriptionStatus();

    // Show/hide history toggle
    if (elements.toggleHistoryBtn) {
        elements.toggleHistoryBtn.style.display = state.planLimits?.history ? 'flex' : 'none';
    }
}

// ================================
// LOAD USER PLAN STATUS
// ================================
async function loadUserStatus() {
    try {
        const res = await fetch(`/api/user-status?_=${Date.now()}`);
        const data = await res.json();
        
        state.isLoggedIn = data.logged_in;
        state.userPlan = data.plan;
        state.planLimits = data.limits;
        state.usedThisMonth = data.used_this_month;
        state.totalProposals = data.total_proposals;
        state.feedbackGiven = data.feedback_given;
        state.subscription = data.subscription || {};
        
        try { updateUIForPlan(); } catch(e) { console.error('UI Error:', e); }
        try { updateButtonStates(); } catch(e) { console.error('UI Error:', e); }
        try { renderSubscriptionStatus(); } catch(e) { console.error('UI Error:', e); }
        try { renderHeaderPlan(); } catch(e) { console.error('UI Error:', e); }
        try { loadFeedbacks(); } catch(e) { console.error('UI Error:', e); }
        
        console.log('DEBUG: User status loaded', { plan: state.userPlan, isLoggedIn: state.isLoggedIn });
        
        if (state.isLoggedIn && state.planLimits.history) {
            loadHistory();
            if (elements.toggleHistoryBtn) elements.toggleHistoryBtn.style.display = 'flex';
        } else {
            if (elements.toggleHistoryBtn) elements.toggleHistoryBtn.style.display = 'none';
        }
    } catch (e) {
        console.error('Error loading user status:', e);
    }
}

function renderSubscriptionStatus() {
    if (!elements.sidebarUserPlan) return;
    
    const plan = (state.userPlan || 'free').toUpperCase();
    const sub = state.subscription || {};
    
    let html = `
        <div style="padding:16px; background:rgba(255,255,255,0.03); border-radius:12px; border:1px solid var(--glass-border);">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <span style="font-size:0.7rem; color:var(--fg-muted); text-transform:uppercase; letter-spacing:0.05em;">Current Plan</span>
                <span class="plan-badge ${state.userPlan}" style="font-size:0.6rem; padding:2px 8px; border-radius:100px; font-weight:700;">${plan}</span>
            </div>
    `;
    
    if (state.userPlan !== 'free' && sub.expiry_date) {
        const expiry = new Date(sub.expiry_date).toLocaleDateString();
        html += `
            <div style="font-size:0.75rem; color:var(--fg-secondary);">
                Expires: <span style="color:var(--fg-primary); font-weight:600;">${expiry}</span>
            </div>
            <div style="font-size:0.65rem; color:var(--fg-muted); margin-top:4px;">
                Status: <span style="color:${sub.status === 'active' ? 'var(--accent-primary)' : '#ef4444'}">${sub.status.toUpperCase()}</span>
            </div>
        `;
    } else if (state.userPlan === 'free') {
        html += `
            <div style="font-size:0.75rem; color:var(--fg-secondary);">
                Basic Access
            </div>
            <a href="#pricing" onclick="toggleSidebar(false)" style="display:inline-block; font-size:0.7rem; color:var(--accent-primary); margin-top:6px; text-decoration:none; font-weight:600;">Upgrade to unlock history →</a>
        `;
    }
    
    html += `</div>`;
    elements.sidebarUserPlan.innerHTML = html;
}

function renderHeaderPlan() {
    const badge = document.getElementById('headerPlanBadge');
    const mobileBadge = document.getElementById('mobilePlanBadge');
    
    if (!badge && !mobileBadge) return;
    
    const plan = (state.userPlan || 'free').toLowerCase();
    const planLabel = plan.toUpperCase();
    
    [badge, mobileBadge].forEach(el => {
        if (!el) return;
        el.textContent = planLabel;
        el.className = `plan-badge-header plan-badge ${plan}`;
        el.style.display = 'inline-block';
    });
}

function updateUsageIndicator(remaining, limit) {
    const genBtn = elements.generateBtn;
    if (!genBtn) return;
    
    // Clear existing note
    const suffix = genBtn.querySelector('.usage-note');
    if (suffix) suffix.remove();
    
    const note = document.createElement('small');
    note.className = 'usage-note';
    note.style.cssText = 'display:block;font-size:0.68rem;opacity:0.7;margin-top:4px;font-weight:400;';

    // Agency / Agent Plan (Unlimited)
    if (state.userPlan === 'agency') {
        note.textContent = "Unlimited Proposals — Keep crushing it! 🚀";
        genBtn.appendChild(note);
        return;
    }

    // Free & Pro Plans (Numeric Limits)
    if (remaining !== null && remaining !== undefined) {
        if (remaining > 0) {
            const planText = state.userPlan === 'free' ? 'free ' : '';
            note.textContent = `${remaining} of ${limit} ${planText}proposals left this month`;
        } else {
            const nextTier = state.userPlan === 'free' ? 'Pro' : 'Agent';
            note.textContent = `Monthly limit reached — upgrade to ${nextTier}`;
        }
        genBtn.appendChild(note);
    }
}

function updateButtonStates() {
    // Grey out buttons that are not in the user's plan
    const buttonFeatureMap = [
        { btn: elements.downloadBtn, feature: 'pdf',  label: 'Download PDF' },
        { btn: elements.sendBtn,     feature: 'send', label: 'Send to Client' },
    ];

    buttonFeatureMap.forEach(({ btn, feature, label }) => {
        if (!btn) return;
        const allowed = state.planLimits[feature] !== false;
        if (!allowed) {
            btn.style.opacity = '0.45';
            btn.title = `Upgrade to Pro to use ${label}`;
            btn.setAttribute('data-locked', 'true');
            btn.setAttribute('data-feature', feature);
            // Add lock icon visually
            if (!btn.querySelector('.lock-icon')) {
                const lock = document.createElement('span');
                lock.className = 'lock-icon';
                lock.innerHTML = ' 🔒';
                lock.style.fontSize = '0.8em';
                btn.appendChild(lock);
            }
        } else {
            btn.style.opacity = '';
            btn.title = '';
            btn.removeAttribute('data-locked');
            const lock = btn.querySelector('.lock-icon');
            if (lock) lock.remove();
        }
    });
}

// ================================
// FEATURE GATE CHECK
// ================================
async function checkFeature(feature) {
    try {
        const res = await fetch('/api/check-feature', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ feature })
        });
        const data = await res.json();
        return data;
    } catch (e) {
        return { allowed: true };
    }
}

// ================================
// RENDER PROPOSAL
// ================================
function renderProposal(proposal) {
    const { client, project, sections } = proposal;
    const fmt = (n) => Number(n).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });

    const milestoneRows = (sections.milestones || []).map(m => `
        <tr>
            <td><strong>${m.title}</strong></td>
            <td>${m.duration}</td>
            <td>
                <ul style="margin:0; padding-left:1.2rem; font-size:0.85rem; color:rgba(255,255,255,0.7);">
                    ${(m.deliverables || []).map(d => `<li>${d}</li>`).join('')}
                </ul>
            </td>
            <td class="milestone-price">$${fmt(m.price)}</td>
        </tr>
    `).join('');

    const toParas = (text) => (text || '').split('\n\n').filter(p => p.trim()).map(p => `<p>${p.trim()}</p>`).join('');

    const html = `
        <div class="proposal-meta">
            <div class="proposal-from">
                <strong>From:</strong>
                Your Name<br>
                Independent Consultant<br>
                your@email.com
            </div>
            <div class="proposal-to">
                <strong>Prepared for:</strong>
                ${client.name}<br>
                ${client.company}<br>
                ${new Date().toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' })}
            </div>
        </div>

        <div class="proposal-section">
            <h2 style="font-size:1.5rem; color:var(--accent-primary); margin-bottom:1.5rem;">${project.title}</h2>
            <h3 class="proposal-section-title">Executive Summary</h3>
            <div class="proposal-section-content">${toParas(sections.executiveSummary)}</div>
        </div>

        <div class="proposal-section">
            <h3 class="proposal-section-title">Scope of Work</h3>
            <div class="proposal-section-content">${toParas(sections.scopeOfWork)}</div>
        </div>

        <div class="proposal-section">
            <h3 class="proposal-section-title">Timeline &amp; Milestones</h3>
            <table class="milestones-table">
                <thead>
                    <tr>
                        <th style="width:25%">Phase</th>
                        <th style="width:15%">Duration</th>
                        <th style="width:40%">Key Deliverables</th>
                        <th style="width:20%">Investment</th>
                    </tr>
                </thead>
                <tbody>${milestoneRows}</tbody>
            </table>
        </div>

        <div class="proposal-total">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <span class="total-label">Total Project Investment</span>
                <span class="total-amount">$${fmt(project.price)}</span>
            </div>
            ${sections.investment.breakdown ? `<p style="font-size:0.875rem; line-height:1.6; opacity:0.9; margin:0;">${sections.investment.breakdown}</p>` : ''}
        </div>

        <div class="proposal-section">
            <h3 class="proposal-section-title">Next Steps</h3>
            <div class="proposal-section-content">${toParas(sections.nextSteps)}</div>
        </div>

    `;

    elements.proposalDocument.innerHTML = html;
}

// ================================
// FORM SUBMISSION
// ================================
elements.form.addEventListener('submit', async (e) => {
    e.preventDefault();
    if (state.isGenerating) return;
    state.isGenerating = true;

    const clientName  = document.getElementById('clientName').value.trim();
    const projectGoal = document.getElementById('projectGoal').value.trim();
    const isPredict   = elements.predictPrice.checked;
    const projectPrice = isPredict ? null : parseFloat(elements.projectPrice.value);
    const timeline    = parseInt(document.getElementById('timeline').value, 10);

    if (!clientName)             { showToast('Please enter the client name.', 'error');        state.isGenerating = false; return; }
    if (!projectGoal)            { showToast('Please describe the project goal.', 'error');    state.isGenerating = false; return; }
    if (!isPredict && (!projectPrice || projectPrice <= 0)) { 
        showToast('Please enter a valid project price or select AI Predict.', 'error'); 
        state.isGenerating = false; 
        return; 
    }

    // Show loading
    elements.generateBtn.classList.add('loading');
    elements.loadingOverlay.classList.add('visible');
    if (elements.statusDot) elements.statusDot.classList.remove('ready');
    if (elements.statusText) elements.statusText.textContent = 'Generating...';

    try {
        const response = await fetch('/api/generate-proposal', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ clientName, projectGoal, projectPrice, timeline })
        });

        const result = await response.json();

        if (result.success && result.proposal) {
            state.currentProposal = result.proposal;
            state.userPlan = result.plan || state.userPlan;
            state.usedThisMonth = result.used_this_month || state.usedThisMonth;

            // Show proposal panel
            if (elements.emptyState)       elements.emptyState.style.display = 'none';
            if (elements.proposalDocument) elements.proposalDocument.classList.add('visible');
            if (elements.previewFooter)    elements.previewFooter.classList.add('visible');
            if (elements.statusDot)        elements.statusDot.classList.add('ready');
            if (elements.statusText)       elements.statusText.textContent = 'Ready to send';

            renderProposal(result.proposal);
            updateButtonStates();  // Re-apply plan gates after generation
            showToast('Proposal generated successfully! 🎉', 'success');

            // Refresh usage indicator
            const remaining = state.planLimits.proposals_per_month
                ? state.planLimits.proposals_per_month - state.usedThisMonth
                : null;
            updateUsageIndicator(remaining, state.planLimits.proposals_per_month);

            // Increment total proposals for feedback check
            state.totalProposals++;
            
            // Trigger Feedback Popup if it's the 1st proposal and feedback not given
            if (state.totalProposals === 1 && !state.feedbackGiven) {
                setTimeout(showFeedbackModal, 2500); // Show after a short delay
            }

        } else if (result.upgrade_required) {
            // Plan limit hit — show upgrade notification
            showToast(result.error, 'upgrade');
            if (elements.statusText) elements.statusText.textContent = 'Limit reached';
        } else {
            throw new Error(result.error || 'Generation failed.');
        }
    } catch (err) {
        console.error('Generation error:', err);
        showToast('Error: ' + err.message, 'error');
        if (elements.statusText) elements.statusText.textContent = 'Error — try again';
    } finally {
        state.isGenerating = false;
        elements.generateBtn.classList.remove('loading');
        elements.loadingOverlay.classList.remove('visible');
        // Refresh history if allowed
        if (state.planLimits.history) loadHistory();
    }
});

// ================================
// ACTION BUTTONS (plan-gated)
// ================================
elements.copyBtn && elements.copyBtn.addEventListener('click', async () => {
    if (!state.currentProposal) { showToast('Generate a proposal first.', 'error'); return; }
    
    // Copy content with better formatting
    const doc = elements.proposalDocument;
    
    // If we have access to the Clipboard API
    if (navigator.clipboard && window.isSecureContext) {
        try {
            // We'll copy as plain text but maintain some structure
            const text = doc.innerText;
            await navigator.clipboard.writeText(text);
            showToast('Proposal copied to clipboard!', 'success');
            return;
        } catch (err) {
            console.error('Clipboard API failed:', err);
        }
    }

    // Fallback: selection method
    try {
        const range = document.createRange();
        range.selectNode(doc);
        window.getSelection().removeAllRanges();
        window.getSelection().addRange(range);
        document.execCommand('copy');
        window.getSelection().removeAllRanges();
        showToast('Proposal copied (fallback)!', 'success');
    } catch (err) {
        showToast('Could not copy. Please select and copy manually.', 'error');
    }
});

elements.downloadBtn && elements.downloadBtn.addEventListener('click', async () => {
    if (!state.currentProposal) { showToast('Generate a proposal first.', 'error'); return; }
    const check = await checkFeature('pdf');
    if (!check.allowed) {
        showToast(check.error, 'upgrade');
        return;
    }

    const element = elements.proposalDocument;
    const opt = {
        margin:       10,
        filename:     `Proposal_${state.currentProposal.project?.title?.replace(/\s+/g, '_') || 'ProposeAI'}.pdf`,
        image:        { type: 'jpeg', quality: 0.98 },
        html2canvas:  { scale: 2, useCORS: true, backgroundColor: '#050505' },
        jsPDF:        { unit: 'mm', format: 'a4', orientation: 'portrait' }
    };

    showToast('Generating PDF...', 'info');
    
    // Temporarily hide elements if needed or adjust styles for PDF
    html2pdf().set(opt).from(element).save()
        .then(() => showToast('PDF downloaded successfully!', 'success'))
        .catch(err => {
            console.error('PDF Error:', err);
            showToast('Failed to generate PDF.', 'error');
        });
});

// ================================
// SEND MODAL LOGIC
// ================================
const sendModal = document.getElementById('sendModal');
const sendModalOverlay = document.getElementById('sendModalOverlay');
const closeSendModal = document.getElementById('closeSendModal');
const sendProposalForm = document.getElementById('sendProposalForm');
const confirmSendBtn = document.getElementById('confirmSendBtn');
const confirmSendText = document.getElementById('confirmSendText');
const confirmSendLoader = document.getElementById('confirmSendLoader');

function hideSendModal() {
    if (sendModal) sendModal.style.display = 'none';
    if (sendModalOverlay) sendModalOverlay.classList.remove('active');
    if (sendProposalForm) sendProposalForm.reset();
}

elements.sendBtn && elements.sendBtn.addEventListener('click', async () => {
    if (!state.currentProposal) { showToast('Generate a proposal first.', 'error'); return; }
    
    const check = await checkFeature('send');
    if (!check.allowed) {
        showToast(check.error, 'upgrade');
        return;
    }

    // Open modal
    if (sendModal) {
        sendModal.style.display = 'flex';
        sendModalOverlay.classList.add('active');
        document.getElementById('recipientInput').focus();
    }
});

closeSendModal && closeSendModal.addEventListener('click', hideSendModal);
sendModalOverlay && sendModalOverlay.addEventListener('click', hideSendModal);

sendProposalForm && sendProposalForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const recipient = document.getElementById('recipientInput').value.trim();
    const password = document.getElementById('authPassword').value;
    
    if (!recipient || !password) return;
    
    const proposalId = state.currentProposal.id || state.currentProposal.proposal_id || 'demo_' + Date.now();
    
    confirmSendBtn.classList.add('loading');
    confirmSendBtn.disabled = true;
    confirmSendText.style.display = 'none';
    confirmSendLoader.style.display = 'block';

    try {
        const response = await fetch('/api/send-proposal', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 
                proposal_id: proposalId,
                recipient: recipient,
                password: password
            })
        });

        const result = await response.json();
        
        if (result.success) {
            showToast('✅ ' + result.message, 'success');
            hideSendModal();
            if (state.planLimits.history) loadHistory();
        } else {
            showToast(result.error || 'Failed to send proposal.', 'error');
            document.getElementById('authPassword').value = '';
            document.getElementById('authPassword').focus();
        }
    } catch (err) {
        console.error('Send error:', err);
        showToast('Network error sending proposal.', 'error');
    } finally {
        confirmSendBtn.classList.remove('loading');
        confirmSendBtn.disabled = false;
        confirmSendText.style.display = 'inline-block';
        confirmSendLoader.style.display = 'none';
    }
});

elements.editBtn && elements.editBtn.addEventListener('click', () => {
    if (!state.currentProposal) return;
    
    state.isEditing = !state.isEditing;
    const sections = elements.proposalDocument.querySelectorAll('.proposal-section-content');
    
    if (state.isEditing) {
        sections.forEach(s => s.setAttribute('contenteditable', 'true'));
        elements.editBtn.textContent = 'Save Changes';
        elements.editBtn.classList.add('editing');
        // Visual indicator
        elements.editBtn.style.background = 'var(--accent-primary)';
        elements.editBtn.style.color = 'var(--bg-primary)';
        showToast('Editing mode enabled. Click sections to modify.', 'success');
        // Focus first section
        if (sections[0]) sections[0].focus();
    } else {
        sections.forEach(s => s.removeAttribute('contenteditable'));
        elements.editBtn.textContent = 'Edit';
        elements.editBtn.classList.remove('editing');
        elements.editBtn.style.background = '';
        elements.editBtn.style.color = '';
        showToast('Changes saved to preview!', 'success');
        
        // Update currentProposal state with edited content (optional but good)
        // For simplicity, we just keep it in the DOM for now.
    }
});

// ================================
// KEYBOARD SHORTCUTS
// ================================
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && elements.loadingOverlay.classList.contains('visible')) {
        elements.loadingOverlay.classList.remove('visible');
        state.isGenerating = false;
        elements.generateBtn.classList.remove('loading');
    }
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
        elements.form.dispatchEvent(new Event('submit'));
    }
});

// ================================
// UPGRADE PLAN
// ================================
async function upgradePlan(plan) {
    // Redirect to the new premium payment page
    window.location.href = `/payment?plan=${plan.toLowerCase()}`;
}

// ================================
// REFINEMENT
// ================================
async function refineProposal(action) {
    if (state.isGenerating || !state.currentProposal) return;
    state.isGenerating = true;

    elements.loadingOverlay.classList.add('visible');
    if (elements.statusText) elements.statusText.textContent = action === 'increase' ? 'Expanding scope...' : 'Optimizing budget...';

    try {
        const response = await fetch('/api/refine-proposal', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ proposal: state.currentProposal, action })
        });

        const result = await response.json();

        if (result.success && result.proposal) {
            state.currentProposal = result.proposal;
            renderProposal(result.proposal);
            showToast(`Proposal ${action === 'increase' ? 'expanded' : 'optimized'}! ✨`, 'success');
        } else {
            throw new Error(result.error || 'Refinement failed.');
        }
    } catch (err) {
        console.error('Refinement error:', err);
        showToast('Error: ' + err.message, 'error');
    } finally {
        state.isGenerating = false;
        elements.loadingOverlay.classList.remove('visible');
    }
}

// ================================
// SIDEBAR & HISTORY LOGIC
// ================================
function toggleSidebar(force) {
    state.sidebarOpen = force !== undefined ? force : !state.sidebarOpen;
    elements.sidebar.classList.toggle('open', state.sidebarOpen);
    elements.sidebarOverlay.classList.toggle('active', state.sidebarOpen);
    document.body.classList.toggle('sidebar-open', state.sidebarOpen);
}

async function loadHistory() {
    if (!elements.historyList) return;
    
    try {
        const res = await fetch(`/api/proposals?_=${Date.now()}`);
        const data = await res.json();
        
        if (data.success && data.proposals) {
            renderHistoryList(data.proposals);
        } else {
            elements.historyList.innerHTML = `<div style="text-align:center;color:var(--fg-muted);font-size:0.8rem;margin-top:20px;">${data.error || 'Failed to load history'}</div>`;
        }
    } catch (e) {
        console.error('Error loading history:', e);
    }
}

function renderHistoryList(proposals) {
    if (proposals.length === 0) {
        elements.historyList.innerHTML = '<div style="text-align:center;color:var(--fg-muted);font-size:0.8rem;margin-top:20px;">No proposals yet.</div>';
        return;
    }

    elements.historyList.innerHTML = proposals.map(p => {
        const date = new Date(p.created_at).toLocaleDateString('en-US', { month: 'short', day: 'numeric' });
        const title = p.generated_output?.project?.title || p.client_name || 'Untitled Proposal';
        
        return `
            <div class="history-item" data-id="${p.proposal_id}" onclick="loadProposalDetail('${p.proposal_id}')">
                <div class="history-item-title">${title}</div>
                <div class="history-item-meta">
                    <span>${p.client_name}</span>
                    <span>${date}</span>
                </div>
                <div class="history-item-actions">
                    <button class="btn-history-action" onclick="event.stopPropagation(); renameProposal('${p.proposal_id}', '${title.replace(/'/g, "\\'")}')" title="Rename">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
                    </button>
                    <button class="btn-history-action delete" onclick="event.stopPropagation(); deleteProposal('${p.proposal_id}')" title="Delete">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg>
                    </button>
                </div>
            </div>
        `;
    }).join('');
}

async function loadProposalDetail(id) {
    // Show loading
    elements.loadingOverlay.classList.add('visible');
    if (elements.statusText) elements.statusText.textContent = 'Loading proposal...';
    
    try {
        const res = await fetch(`/api/proposal/${id}?_=${Date.now()}`);
        const data = await res.json();
        
        if (data.success && data.proposal) {
            state.currentProposal = data.proposal;
            
            // Hide empty state
            if (elements.emptyState) elements.emptyState.style.display = 'none';
            if (elements.proposalDocument) elements.proposalDocument.classList.add('visible');
            if (elements.previewFooter) elements.previewFooter.classList.add('visible');
            if (elements.statusDot) elements.statusDot.classList.add('ready');
            if (elements.statusText) elements.statusText.textContent = 'History Item Loaded';
            
            renderProposal(data.proposal);
            
            // Highlight active item
            document.querySelectorAll('.history-item').forEach(el => {
                el.classList.toggle('active', el.getAttribute('data-id') === id);
            });

            // Close sidebar on mobile
            if (window.innerWidth < 1024) toggleSidebar(false);
            
            showToast('Proposal loaded from history!', 'success');
        } else {
            showToast(data.error || 'Failed to load proposal.', 'error');
        }
    } catch (e) {
        showToast('Network error loading proposal.', 'error');
    } finally {
        elements.loadingOverlay.classList.remove('visible');
    }
}

async function renameProposal(id, currentTitle) {
    const newTitle = prompt('Enter new title for the proposal:', currentTitle);
    if (!newTitle || newTitle.trim() === '' || newTitle.trim() === currentTitle) return;

    try {
        console.log(`DEBUG: Renaming proposal ${id} to ${newTitle}`);
        const res = await fetch(`/api/proposal/${id}/rename?_=${Date.now()}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title: newTitle.trim() })
        });
        const data = await res.json();
        console.log('DEBUG: Rename response:', data);
        
        if (data.success) {
            showToast('Proposal renamed successfully!', 'success');
            loadHistory(); // Refresh list
            
            // If renamed item is currently loaded, update the UI
            if (state.currentProposal && state.currentProposal.id === id) {
                // Current proposal state in main.js uses 'id' instead of 'proposal_id' sometimes depending on context
                // but app.py returns proposal_id. Let's ensure consistency.
                if (state.currentProposal.project) {
                    state.currentProposal.project.title = newTitle.trim();
                    renderProposal(state.currentProposal);
                }
            }
        } else {
            showToast(data.error || 'Failed to rename proposal.', 'error');
        }
    } catch (e) {
        showToast('Network error renaming proposal.', 'error');
    }
}

async function deleteProposal(id) {
    if (!confirm('Are you sure you want to delete this proposal? This action cannot be undone.')) return;

    try {
        console.log(`DEBUG: Deleting proposal ${id}`);
        const res = await fetch(`/api/proposal/${id}?_=${Date.now()}`, {
            method: 'DELETE'
        });
        const data = await res.json();
        console.log('DEBUG: Delete response:', data);
        
        if (data.success) {
            showToast('Proposal deleted successfully!', 'success');
            loadHistory(); // Refresh list
            
            // If deleted item was currently loaded, clear preview
            // Note: app.py stores generated_output inside doc, and generated_output has its own id.
            // When loading detail, we set state.currentProposal = data.proposal (which is doc["generated_output"])
            if (state.currentProposal && (state.currentProposal.id === id || state.currentProposal.proposal_id === id)) {
                state.currentProposal = null;
                if (elements.emptyState) elements.emptyState.style.display = 'flex';
                if (elements.proposalDocument) elements.proposalDocument.classList.remove('visible');
                if (elements.previewFooter) elements.previewFooter.classList.remove('visible');
                if (elements.statusDot) elements.statusDot.classList.remove('ready');
                if (elements.statusText) elements.statusText.textContent = 'Waiting for input';
            }
        } else {
            showToast(data.error || 'Failed to delete proposal.', 'error');
        }
    } catch (e) {
        showToast('Network error deleting proposal.', 'error');
    }
}

// ================================
// INIT
// ================================
document.addEventListener('DOMContentLoaded', () => {
    loadUserStatus();

    // AI Predict Toggle
    if (elements.predictPrice) {
        elements.predictPrice.addEventListener('change', (e) => {
            elements.projectPrice.disabled = e.target.checked;
            elements.projectPrice.style.opacity = e.target.checked ? '0.5' : '1';
            if (e.target.checked) elements.projectPrice.value = '';
        });
    }

    // Refinement Buttons
    if (elements.increaseBtn) elements.increaseBtn.addEventListener('click', () => refineProposal('increase'));
    if (elements.decreaseBtn) elements.decreaseBtn.addEventListener('click', () => refineProposal('decrease'));

    // Sidebar Listeners
    if (elements.sidebarToggleBtn) elements.sidebarToggleBtn.addEventListener('click', () => toggleSidebar());
    if (elements.toggleHistoryBtn) elements.toggleHistoryBtn.addEventListener('click', () => toggleSidebar());
    if (elements.closeSidebar) elements.closeSidebar.addEventListener('click', () => toggleSidebar(false));
    if (elements.sidebarOverlay) elements.sidebarOverlay.addEventListener('click', () => toggleSidebar(false));
    
    if (elements.newProposalBtn) {
        elements.newProposalBtn.addEventListener('click', () => {
            state.currentProposal = null;
            elements.form.reset();
            if (elements.emptyState) elements.emptyState.style.display = 'flex';
            if (elements.proposalDocument) elements.proposalDocument.classList.remove('visible');
            if (elements.previewFooter) elements.previewFooter.classList.remove('visible');
            if (elements.statusDot) elements.statusDot.classList.remove('ready');
            if (elements.statusText) elements.statusText.textContent = 'Waiting for input';
            toggleSidebar(false);
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // Mobile Nav Toggle
    if (elements.hamburgerBtn && elements.mobileNav) {
        elements.hamburgerBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            elements.mobileNav.classList.toggle('open');
            // Change hamburger icon to X or keep as is? 
            // Let's just toggle for now.
        });

        // Close when clicking links
        elements.mobileNav.querySelectorAll('.mobile-nav-link').forEach(link => {
            link.addEventListener('click', () => {
                elements.mobileNav.classList.remove('open');
            });
        });

        // Close when clicking outside
        document.addEventListener('click', (e) => {
            if (elements.mobileNav.classList.contains('open') && 
                !elements.mobileNav.contains(e.target) && 
                !elements.hamburgerBtn.contains(e.target)) {
                elements.mobileNav.classList.remove('open');
            }
        });
    }
});

console.log('ProposeAI JS loaded ✅');


// ================================
// FEEDBACK SYSTEM
// ================================
function showFeedbackModal() {
    if (elements.feedbackModal) {
        elements.feedbackModal.style.display = 'flex';
        elements.feedbackModalOverlay.classList.add('active');
    }
}

function hideFeedbackModal() {
    if (elements.feedbackModal) {
        elements.feedbackModal.style.display = 'none';
        elements.feedbackModalOverlay.classList.remove('active');
    }
}

elements.closeFeedbackModal && elements.closeFeedbackModal.addEventListener('click', hideFeedbackModal);
elements.feedbackModalOverlay && elements.feedbackModalOverlay.addEventListener('click', hideFeedbackModal);

elements.feedbackForm && elements.feedbackForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const features = document.getElementById('feedbackFeatures').value.trim();
    const bugs = document.getElementById('feedbackBugs').value.trim();

    try {
        const res = await fetch('/api/feedback', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ features, bugs })
        });
        const data = await res.json();
        if (data.success) {
            showToast(data.message, 'success');
            state.feedbackGiven = true;
            hideFeedbackModal();
            loadFeedbacks(); // Refresh the wall
        } else {
            showToast(data.error || 'Failed to send feedback.', 'error');
        }
    } catch (err) {
        showToast('Network error.', 'error');
    }
});

async function loadFeedbacks() {
    if (!elements.feedbackContainer) return;
    try {
        const res = await fetch('/api/feedbacks');
        const data = await res.json();
        if (data.success && data.feedbacks) {
            renderFeedbackWall(data.feedbacks);
        }
    } catch (err) {
        console.error('Error loading feedbacks:', err);
    }
}

function renderFeedbackWall(feedbacks) {
    if (!elements.feedbackContainer) return;
    if (feedbacks.length === 0) {
        elements.feedbackContainer.innerHTML = '<div class="glass-card" style="padding: 24px; text-align: center; color: var(--fg-muted); grid-column: 1/-1;">Be the first to leave feedback! ✨</div>';
        return;
    }

    elements.feedbackContainer.innerHTML = feedbacks.map(f => {
        const date = f.created_at ? new Date(f.created_at).toLocaleDateString() : 'Recently';
        return `
            <div class="glass-card reveal" style="padding: 24px; display: flex; flex-direction: column; gap: 12px; transition: transform 0.3s ease;">
                <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                    <div style="font-weight: 700; color: var(--accent-primary); font-size: 0.9rem;">@${f.user_name}</div>
                    <div style="font-size: 0.7rem; color: var(--fg-muted);">${date}</div>
                </div>
                <div style="color: var(--fg-primary); font-size: 0.95rem; line-height: 1.5; font-style: italic;">
                    "${f.features || 'Stunning experience!'}"
                </div>
                ${f.bugs ? `<div style="font-size: 0.8rem; color: var(--fg-secondary); padding: 8px; background: rgba(255,255,255,0.03); border-radius: 6px;">
                    <span style="color: #ff4444; font-weight: 700; font-size: 0.7rem; text-transform: uppercase;">Bug reported:</span> ${f.bugs}
                </div>` : ''}
            </div>
        `;
    }).join('');
    
    // Trigger reveals for new cards
    if (window.initPremiumInteractions) window.initPremiumInteractions();
}


// Initialize any missing pieces
window.addEventListener('DOMContentLoaded', () => {
    // Ensure history logic is loaded if allowed
    if (state.isLoggedIn && state.planLimits?.history) {
        loadHistory();
    }
});

// ================================
// CONTACT FORM HANDLER
// ================================
async function handleContactSubmit(event) {
    event.preventDefault();
    const btn = document.getElementById('contactSubmitBtn');
    const btnText = document.getElementById('contactBtnText');
    const originalText = btnText.innerHTML;

    // Show loading state
    btn.disabled = true;
    btnText.innerHTML = '<span class="btn-loader" style="display:inline-block; position:static; margin:0 auto;"></span> Sending...';

    const name = document.getElementById('contactName').value;
    const email = document.getElementById('contactEmail').value;
    const subject = document.getElementById('contactSubject').value;
    const message = document.getElementById('contactMessage').value;

    try {
        const res = await fetch('/api/contact', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, email, subject, message })
        });
        
        const data = await res.json();
        
        if (data.success) {
            showToast(data.message || `Thanks ${name}! We've received your message.`, 'success');
            event.target.reset();
        } else {
            showToast(data.error || 'Failed to send message.', 'error');
        }
    } catch (err) {
        console.error('Contact Form Error:', err);
        showToast('Network error. Please try again later.', 'error');
    } finally {
        btn.disabled = false;
        btnText.innerHTML = originalText;
    }
}
