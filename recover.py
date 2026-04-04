import os

file_path = r"g:\Proposal\templates\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

top_part = content.split('        <div class="gradient-orb orb-2"></div>')[0] + '        <div class="gradient-orb orb-2"></div>\n'
bottom_part = '                const centerY = window.innerHeight / 2;\n' + content.split('                const centerY = window.innerHeight / 2;\n')[1]

recovered_text = """        <div class="gradient-orb orb-3"></div>
    </div>
    <div class="grid-pattern" aria-hidden="true"></div>
    <div class="noise-overlay" aria-hidden="true"></div>

    <!-- Navigation -->
    <nav class="nav-container reveal stagger-1" role="navigation" aria-label="Main navigation">
        <div class="nav-inner">
            <a href="/" class="logo" style="text-decoration:none;color:inherit;">
                <div class="logo-icon">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"
                        stroke-linecap="round" stroke-linejoin="round">
                        <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z" />
                        <polyline points="14 2 14 8 20 8" />
                        <line x1="16" y1="13" x2="8" y2="13" />
                        <line x1="16" y1="17" x2="8" y2="17" />
                        <line x1="10" y1="9" x2="8" y2="9" />
                    </svg>
                </div>
                ProposeAI
            </a>
            <div class="nav-links">
                <a href="javascript:void(0)" id="toggleHistoryBtn" class="nav-link" style="display:none;">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right:6px;"><path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                    History
                </a>
                <a href="#features" class="nav-link">Features</a>
                <a href="#pricing" class="nav-link">Pricing</a>
                <a href="#templates" class="nav-link">Templates</a>
                <span id="headerPlanBadge" class="plan-badge-header"></span>
                {% if user %}
                    <span class="nav-link" style="color:var(--accent);font-weight:600;">Hi, {{ user.name }}</span>
                    <a href="/logout" class="btn-nav">Log Out</a>
                {% else %}
                    <a href="/login" class="btn-nav" aria-label="Log in">Log In</a>
                    <a href="/login" class="btn-nav btn-nav-primary" aria-label="Start free trial">Start Free</a>
                {% endif %}
            </div>
        </div>
    </nav>

    <!-- Sidebar -->
    <div class="sidebar-overlay" id="sidebarOverlay"></div>
    <aside class="sidebar" id="sidebar">
        <div class="sidebar-header">
            <div class="sidebar-title">Proposals</div>
            <button id="closeSidebar" style="background:none;border:none;color:var(--fg-muted);cursor:pointer;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
            </button>
        </div>
        
        <button class="btn-new-proposal" id="newProposalBtn">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
            New Proposal
        </button>

        <div class="history-list" id="historyList">
            <!-- Loaded via JS -->
            <div style="text-align:center;color:var(--fg-muted);font-size:0.8rem;margin-top:20px;">
                History is a Pro feature
            </div>
        </div>

        <div class="sidebar-footer">
            <div id="sidebarUserPlan">
                <!-- User Plan Badge -->
            </div>
        </div>
    </aside>

    <button id="sidebarToggleBtn" class="sidebar-toggle-btn" title="Toggle History">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
    </button>

    <!-- Main Content -->
    <main class="main-content">
        <section class="hero-section reveal stagger-2">
            <div class="hero-badge">
                <span class="hero-badge-dot" aria-hidden="true"></span>
                AI-Powered Proposals
            </div>
            <h1 class="hero-title">
                Turn 3 Lines Into a<br>
                <span class="hero-title-accent">$5,000 Proposal</span>
            </h1>
            <p class="hero-subtitle">
                Stop losing clients to amateur proposals. Generate premium, legally-sound proposals
                with clear scope, milestones, and integrated sign-and-pay in 90 seconds.
            </p>

            <!-- Dashboard Grid -->
            <div class="dashboard-grid reveal stagger-3">
                <!-- Input Panel -->
                <div class="glass-card input-panel">
                    <div class="panel-header">
                        <div class="panel-icon">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M12 20h9" />
                                <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z" />
                            </svg>
                        </div>
                        <div>
                            <h2 class="panel-title">Describe Your Project</h2>
                            <p class="panel-subtitle">Just 3 lines. We'll handle the rest.</p>
                        </div>
                    </div>

                    <form id="proposalForm">
                        <div class="form-group">
                            <label for="clientName" class="form-label">Client Name</label>
                            <input type="text" id="clientName" class="form-input" placeholder="e.g., Sarah at TechCorp"
                                required aria-required="true">
                        </div>

                        <div class="form-group">
                            <label for="projectGoal" class="form-label">Project Goal</label>
                            <textarea id="projectGoal" class="form-input form-textarea"
                                placeholder="e.g., Build a modern e-commerce platform with React and Node.js, including payment integration and inventory management"
                                required aria-required="true"></textarea>
                        </div>

                        <div class="form-group">
                            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                                <label for="projectPrice" class="form-label" style="margin-bottom:0;">Project Investment</label>
                                <label style="display:inline-flex; align-items:center; gap:6px; font-size:0.7rem; color:var(--accent-primary); cursor:pointer;">
                                    <input type="checkbox" id="predictPrice" style="accent-color:var(--accent-primary);"> 
                                    AI Predict
                                </label>
                            </div>
                            <div class="input-with-prefix" id="priceInputWrapper">
                                <span class="input-prefix">$</span>
                                <input type="number" id="projectPrice" class="form-input" placeholder="5,000" min="100">
                            </div>
                        </div>

                        <div class="form-group">
                            <label for="timeline" class="form-label">Timeline (weeks)</label>
                            <input type="number" id="timeline" class="form-input" placeholder="4" min="1" max="52"
                                value="4" required aria-required="true">
                        </div>

                        <button type="submit" class="btn-generate" id="generateBtn">
                            <span class="btn-text">Generate Premium Proposal</span>
                            <span class="btn-loader" aria-hidden="true"></span>
                            <svg class="btn-icon-arrow" width="20" height="20" viewBox="0 0 24 24" fill="none"
                                stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                                <line x1="5" y1="12" x2="19" y2="12" />
                                <polyline points="12 5 19 12 12 19" />
                            </svg>
                        </button>
                    </form>
                </div>

                <!-- Preview Panel -->
                <div class="glass-card preview-panel">
                    <div class="preview-header">
                        <div class="preview-status">
                            <span class="status-dot" id="statusDot"></span>
                            <span id="statusText">Waiting for input</span>
                        </div>
                        <div class="preview-actions">
                            <button class="btn-icon" aria-label="Copy to clipboard" id="copyBtn"
                                title="Copy to clipboard">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                    stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <rect x="9" y="9" width="13" height="13" rx="2" ry="2" />
                                    <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1" />
                                </svg>
                            </button>
                            <button class="btn-icon" aria-label="Download PDF" id="downloadBtn" title="Download PDF">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                    stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
                                    <polyline points="7 10 12 15 17 10" />
                                    <line x1="12" y1="15" x2="12" y2="3" />
                                </svg>
                            </button>
                        </div>
                    </div>

                    <div class="preview-content" id="previewContent">
                        <!-- Empty State -->
                        <div class="preview-empty" id="emptyState">
                            <div class="preview-empty-icon">
                                <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                    stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z" />
                                    <polyline points="14 2 14 8 20 8" />
                                </svg>
                            </div>
                            <h3 class="preview-empty-title">Your proposal will appear here</h3>
                            <p>Fill in the details and click generate to create your premium proposal.</p>
                        </div>

                        <!-- Proposal Document -->
                        <div class="proposal-document" id="proposalDocument">
                            <!-- Content injected by JS -->
                        </div>
                    </div>

                    <div class="preview-footer" id="previewFooter">
                        <div class="refinement-toolbar" style="display:flex; gap:8px;">
                            <button class="btn-secondary" id="decreaseBtn" title="Decrease Budget & Scope">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 15 12 21 18 15"/><polyline points="6 9 12 15 18 9"/></svg>
                                20%
                            </button>
                            <button class="btn-secondary" id="increaseBtn" title="Increase Budget & Scope">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"/><polyline points="18 9 12 3 6 9"/></svg>
                                20%
                            </button>
                        </div>
                        <div style="display:flex; gap:12px;">
                            <button class="btn-secondary" id="editBtn">Edit</button>
                            <button class="btn-primary" id="sendBtn">Send Proposal</button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Metrics Strip -->
            <div class="metrics-strip reveal stagger-4">
                <div class="metric-item">
                    <div class="metric-value">90<span>sec</span></div>
                    <div class="metric-label">Average generation time</div>
                </div>
                <div class="metric-item">
                    <div class="metric-value">73<span>%</span></div>
                    <div class="metric-label">Higher win rate vs. manual</div>
                </div>
                <div class="metric-item">
                    <div class="metric-value">$2.4<span>k</span></div>
                    <div class="metric-label">Avg. project value won</div>
                </div>
            </div>
        </section>

        <!-- ============================
             FEATURES SECTION
             ============================ -->
        <section id="features" style="padding:100px 40px;max-width:1400px;margin:0 auto;">
            <div class="reveal" style="text-align:center;margin-bottom:64px;">
                <div class="hero-badge" style="display:inline-flex;margin-bottom:24px;">
                    <span class="hero-badge-dot" aria-hidden="true"></span>
                    Why ProposeAI
                </div>
                <h2 style="font-family:'Space Grotesk',sans-serif;font-size:clamp(1.8rem,4vw,3rem);font-weight:700;line-height:1.1;margin-bottom:16px;">
                    Everything you need to win<br>
                    <span style="background:linear-gradient(135deg,var(--accent-primary),#00ff88);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">high-value clients</span>
                </h2>
                <p style="font-size:1.1rem;color:var(--fg-secondary);max-width:560px;margin:0 auto;">Stop losing deals to unprofessional proposals. ProposeAI levels the playing field for independent freelancers.</p>
            </div>

            <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px;">
                <!-- Feature 1 -->
                <div class="glass-card reveal" style="padding:32px;">
                    <div style="width:48px;height:48px;background:linear-gradient(135deg,rgba(0,212,170,0.2),rgba(0,212,170,0.05));border-radius:12px;display:flex;align-items:center;justify-content:center;margin-bottom:20px;color:var(--accent-primary);">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
                    </div>
                    <h3 style="font-size:1.1rem;font-weight:700;margin-bottom:10px;">AI-Powered Generation</h3>
                    <p style="font-size:0.9rem;color:var(--fg-secondary);line-height:1.6;">Enter 3 lines. Get a 5-page, professionally structured proposal in under 90 seconds — every time.</p>
                </div>
                <!-- Feature 2 -->
                <div class="glass-card reveal stagger-1" style="padding:32px;">
                    <div style="width:48px;height:48px;background:linear-gradient(135deg,rgba(0,212,170,0.2),rgba(0,212,170,0.05));border-radius:12px;display:flex;align-items:center;justify-content:center;margin-bottom:20px;color:var(--accent-primary);">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
                    </div>
                    <h3 style="font-size:1.1rem;font-weight:700;margin-bottom:10px;">Milestone Breakdown</h3>
                    <p style="font-size:0.9rem;color:var(--fg-secondary);line-height:1.6;">Auto-generates smart milestones, deliverables, and per-phase pricing based on your timeline and budget.</p>
                </div>
                <!-- Feature 3 -->
                <div class="glass-card reveal stagger-2" style="padding:32px;">
                    <div style="width:48px;height:48px;background:linear-gradient(135deg,rgba(0,212,170,0.2),rgba(0,212,170,0.05));border-radius:12px;display:flex;align-items:center;justify-content:center;margin-bottom:20px;color:var(--accent-primary);">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.17 11a19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 3.08 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.574 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                    </div>
                    <h3 style="font-size:1.1rem;font-weight:700;margin-bottom:10px;">Send & Sign</h3>
                    <p style="font-size:0.9rem;color:var(--fg-secondary);line-height:1.6;">One-click send to your client with a built-in "Sign & Pay" CTA that drives faster conversions.</p>
                </div>
                <!-- Feature 4 -->
                <div class="glass-card reveal" style="padding:32px;">
                    <div style="width:48px;height:48px;background:linear-gradient(135deg,rgba(0,212,170,0.2),rgba(0,212,170,0.05));border-radius:12px;display:flex;align-items:center;justify-content:center;margin-bottom:20px;color:var(--accent-primary);">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
                    </div>
                    <h3 style="font-size:1.1rem;font-weight:700;margin-bottom:10px;">PDF Export</h3>
                    <p style="font-size:0.9rem;color:var(--fg-secondary);line-height:1.6;">Export a pixel-perfect PDF proposal ready to send via email or WhatsApp in one click.</p>
                </div>
                <!-- Feature 5 -->
                <div class="glass-card reveal stagger-1" style="padding:32px;">
                    <div style="width:48px;height:48px;background:linear-gradient(135deg,rgba(0,212,170,0.2),rgba(0,212,170,0.05));border-radius:12px;display:flex;align-items:center;justify-content:center;margin-bottom:20px;color:var(--accent-primary);">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
                    </div>
                    <h3 style="font-size:1.1rem;font-weight:700;margin-bottom:10px;">Proposal History</h3>
                    <p style="font-size:0.9rem;color:var(--fg-secondary);line-height:1.6;">All your proposals are saved with Draft/Sent/Signed statuses so you never lose track of a deal.</p>
                </div>
                <!-- Feature 6 -->
                <div class="glass-card reveal stagger-2" style="padding:32px;">
                    <div style="width:48px;height:48px;background:linear-gradient(135deg,rgba(0,212,170,0.2),rgba(0,212,170,0.05));border-radius:12px;display:flex;align-items:center;justify-content:center;margin-bottom:20px;color:var(--accent-primary);">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
                    </div>
                    <h3 style="font-size:1.1rem;font-weight:700;margin-bottom:10px;">Multi-Currency & INR</h3>
                    <p style="font-size:0.9rem;color:var(--fg-secondary);line-height:1.6;">Works with any currency — perfect for Indian freelancers pitching to US/UK/EU clients.</p>
                </div>
            </div>
        </section>

        <!-- ============================
             PRICING SECTION
             ============================ -->
        <section id="pricing" style="padding:100px 40px;max-width:1400px;margin:0 auto;">
            <div class="reveal" style="text-align:center;margin-bottom:64px;">
                <div class="hero-badge" style="display:inline-flex;margin-bottom:24px;">
                    <span class="hero-badge-dot" aria-hidden="true"></span>
                    Simple Pricing
                </div>
                <h2 style="font-family:'Space Grotesk',sans-serif;font-size:clamp(1.8rem,4vw,3rem);font-weight:700;line-height:1.1;margin-bottom:16px;">
                    One proposal win pays for<br>
                    <span style="background:linear-gradient(135deg,var(--accent-primary),#00ff88);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">a full year</span>
                </h2>
                <p style="font-size:1.1rem;color:var(--fg-secondary);max-width:500px;margin:0 auto;">No hidden fees. Cancel anytime. Start free, upgrade when you're ready.</p>
            </div>

            <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px;max-width:960px;margin:0 auto;">
                <!-- Free Plan -->
                <div class="glass-card reveal" style="padding:40px;text-align:center;">
                    <div style="font-size:0.75rem;font-weight:700;text-transform:uppercase;letter-spacing:0.1em;color:var(--fg-muted);margin-bottom:12px;">Free</div>
                    <div style="font-family:'Space Grotesk',sans-serif;font-size:3rem;font-weight:700;margin-bottom:4px;">$0</div>
                    <div style="font-size:0.875rem;color:var(--fg-secondary);margin-bottom:32px;">Forever free</div>
                    <ul style="list-style:none;text-align:left;margin-bottom:32px;display:flex;flex-direction:column;gap:12px;">
                        <li style="font-size:0.9rem;color:var(--fg-secondary);display:flex;align-items:center;gap:10px;"><span style="color:var(--accent-primary);">✓</span> 3 proposals/month</li>
                        <li style="font-size:0.9rem;color:var(--fg-secondary);display:flex;align-items:center;gap:10px;"><span style="color:var(--accent-primary);">✓</span> All sections included</li>
                        <li style="font-size:0.9rem;color:var(--fg-secondary);display:flex;align-items:center;gap:10px;"><span style="color:var(--accent-primary);">✓</span> Copy & PDF export</li>
                        <li style="font-size:0.9rem;color:var(--fg-muted);display:flex;align-items:center;gap:10px;"><span>✗</span> Proposal history</li>
                    </ul>
                    <a href="javascript:void(0)" onclick="upgradePlan('free')" style="display:block;padding:14px;border:1px solid var(--glass-border);border-radius:10px;color:var(--fg-primary);text-decoration:none;font-weight:600;font-size:0.9rem;transition:all 0.3s;" onmouseover="this.style.borderColor='var(--accent-primary)'" onmouseout="this.style.borderColor='var(--glass-border)'">Get Started Free</a>
                </div>

                <!-- Pro Plan -->
                <div class="glass-card reveal stagger-1" style="padding:40px;text-align:center;border-color:var(--accent-primary);position:relative;box-shadow:0 0 40px var(--accent-glow);">
                    <div style="position:absolute;top:-14px;left:50%;transform:translateX(-50%);background:linear-gradient(135deg,var(--accent-primary),var(--accent-secondary));padding:4px 16px;border-radius:100px;font-size:0.7rem;font-weight:700;color:#050505;text-transform:uppercase;letter-spacing:0.08em;">Most Popular</div>
                    <div style="font-size:0.75rem;font-weight:700;text-transform:uppercase;letter-spacing:0.1em;color:var(--accent-primary);margin-bottom:12px;">Pro</div>
                    <div style="font-family:'Space Grotesk',sans-serif;font-size:3rem;font-weight:700;margin-bottom:4px;">$9<span style="font-size:1.2rem;color:var(--fg-secondary);">/mo</span></div>
                    <div style="font-size:0.875rem;color:var(--fg-secondary);margin-bottom:32px;">Billed monthly</div>
                    <ul style="list-style:none;text-align:left;margin-bottom:32px;display:flex;flex-direction:column;gap:12px;">
                        <li style="font-size:0.9rem;color:var(--fg-secondary);display:flex;align-items:center;gap:10px;"><span style="color:var(--accent-primary);">✓</span> 100 proposals/month</li>
                        <li style="font-size:0.9rem;color:var(--fg-secondary);display:flex;align-items:center;gap:10px;"><span style="color:var(--accent-primary);">✓</span> All sections included</li>
                        <li style="font-size:0.9rem;color:var(--fg-secondary);display:flex;align-items:center;gap:10px;"><span style="color:var(--accent-primary);">✓</span> PDF export & Send</li>
                        <li style="font-size:0.9rem;color:var(--fg-secondary);display:flex;align-items:center;gap:10px;"><span style="color:var(--accent-primary);">✓</span> Full proposal history</li>
                        <li style="font-size:0.9rem;color:var(--fg-secondary);display:flex;align-items:center;gap:10px;"><span style="color:var(--accent-primary);">✓</span> Custom branding</li>
                    </ul>
                    <a href="javascript:void(0)" onclick="upgradePlan('pro')" style="display:block;padding:14px;background:linear-gradient(135deg,var(--accent-primary),var(--accent-secondary));border-radius:10px;color:#050505;text-decoration:none;font-weight:700;font-size:0.9rem;transition:all 0.3s;" onmouseover="this.style.transform='translateY(-2px)';this.style.boxShadow='0 8px 24px var(--accent-glow)'" onmouseout="this.style.transform='';this.style.boxShadow=''">Upgrade to Pro</a>
                </div>

                <!-- Agency Plan -->
                <div class="glass-card reveal stagger-2" style="padding:40px;text-align:center;">
                    <div style="font-size:0.75rem;font-weight:700;text-transform:uppercase;letter-spacing:0.1em;color:var(--fg-muted);margin-bottom:12px;">Agency</div>
                    <div style="font-family:'Space Grotesk',sans-serif;font-size:3rem;font-weight:700;margin-bottom:4px;">$29<span style="font-size:1.2rem;color:var(--fg-secondary);">/mo</span></div>
                    <div style="font-size:0.875rem;color:var(--fg-secondary);margin-bottom:32px;">Up to 5 seats</div>
                    <ul style="list-style:none;text-align:left;margin-bottom:32px;display:flex;flex-direction:column;gap:12px;">
                        <li style="font-size:0.9rem;color:var(--fg-secondary);display:flex;align-items:center;gap:10px;"><span style="color:var(--accent-primary);">✓</span> Unlimited proposals</li>
                        <li style="font-size:0.9rem;color:var(--fg-secondary);display:flex;align-items:center;gap:10px;"><span style="color:var(--accent-primary);">✓</span> 5 team members</li>
                        <li style="font-size:0.9rem;color:var(--fg-secondary);display:flex;align-items:center;gap:10px;"><span style="color:var(--accent-primary);">✓</span> White-label proposals</li>
                        <li style="font-size:0.9rem;color:var(--fg-secondary);display:flex;align-items:center;gap:10px;"><span style="color:var(--accent-primary);">✓</span> Priority support</li>
                    </ul>
                    <a href="javascript:void(0)" onclick="upgradePlan('agency')" style="display:block;padding:14px;border:1px solid var(--glass-border);border-radius:10px;color:var(--fg-primary);text-decoration:none;font-weight:600;font-size:0.9rem;transition:all 0.3s;" onmouseover="this.style.borderColor='var(--accent-primary)'" onmouseout="this.style.borderColor='var(--glass-border)'">Get Started</a>
                </div>
            </div>
        </section>

        <!-- ============================
             TEMPLATES SECTION
             ============================ -->
        <section id="templates" style="padding:100px 40px;max-width:1400px;margin:0 auto;">
            <div class="reveal" style="text-align:center;margin-bottom:64px;">
                <div class="hero-badge" style="display:inline-flex;margin-bottom:24px;">
                    <span class="hero-badge-dot" aria-hidden="true"></span>
                    Proposal Templates
                </div>
                <h2 style="font-family:'Space Grotesk',sans-serif;font-size:clamp(1.8rem,4vw,3rem);font-weight:700;line-height:1.1;margin-bottom:16px;">
                    Start from a template.<br>
                    <span style="background:linear-gradient(135deg,var(--accent-primary),#00ff88);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">Win even faster.</span>
                </h2>
                <p style="font-size:1.1rem;color:var(--fg-secondary);max-width:540px;margin:0 auto;">Pre-built templates for the most common freelance projects — just fill in your client details.</p>
            </div>

            <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:20px;">
                {% set templates = [
                    {"icon": "🌐", "title": "Web Development", "desc": "Full-stack web app or landing page projects.", "tags": ["React", "Node.js", "API"]},
                    {"icon": "📱", "title": "Mobile App", "desc": "iOS and Android app development proposals.", "tags": ["Flutter", "React Native"]},
                    {"icon": "🎨", "title": "UI/UX Design", "desc": "Product design, wireframes and Figma projects.", "tags": ["Figma", "Branding"]},
                    {"icon": "📈", "title": "Digital Marketing", "desc": "SEO, paid ads, and social media campaigns.", "tags": ["SEO", "Meta Ads", "Google"]},
                    {"icon": "✍️", "title": "Content Writing", "desc": "Blog posts, copywriting and ghostwriting.", "tags": ["Blogs", "Copywriting"]},
                    {"icon": "🤖", "title": "AI & Automation", "desc": "Custom AI tools and workflow automations.", "tags": ["Python", "GPT", "N8N"]}
                ] %}
                {% for t in templates %}
                <div class="glass-card reveal" style="padding:28px;cursor:pointer;transition:all 0.3s ease;"
                     onclick="document.getElementById('clientName').focus();document.getElementById('projectGoal').value='{{ t.title }} project — ';window.scrollTo({top:0,behavior:'smooth'});"
                     onmouseover="this.style.borderColor='var(--accent-primary)';this.style.transform='translateY(-4px)'"
                     onmouseout="this.style.borderColor='var(--glass-border)';this.style.transform=''">
                    <div style="font-size:2rem;margin-bottom:14px;">{{ t.icon }}</div>
                    <h3 style="font-size:1rem;font-weight:700;margin-bottom:8px;">{{ t.title }}</h3>
                    <p style="font-size:0.85rem;color:var(--fg-secondary);margin-bottom:16px;line-height:1.5;">{{ t.desc }}</p>
                    <div style="display:flex;flex-wrap:wrap;gap:6px;">
                        {% for tag in t.tags %}
                        <span style="padding:3px 10px;background:rgba(0,212,170,0.1);border:1px solid rgba(0,212,170,0.2);border-radius:100px;font-size:0.7rem;font-weight:600;color:var(--accent-primary);">{{ tag }}</span>
                        {% endfor %}
                    </div>
                </div>
                {% endfor %}
            </div>
        </section>

        <!-- Detailed Footer -->
        <footer style="border-top: 1px solid var(--glass-border); padding: 80px 40px 40px; background: rgba(5,5,5,0.4); backdrop-filter: blur(10px); margin-top: 60px;">
            <div class="reveal" style="max-width: 1400px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 48px; margin-bottom: 64px;">
                <!-- Column 1: Brand & About -->
                <div style="grid-column: span 1.5;">
                    <div class="logo" style="margin-bottom: 24px;">
                        <div class="logo-icon">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z" />
                                <polyline points="14 2 14 8 20 8" />
                            </svg>
                        </div>
                        ProposeAI
                    </div>
                    <p style="font-size: 0.95rem; color: var(--fg-secondary); line-height: 1.6; max-width: 320px; margin-bottom: 24px;">
                        Transforming the way freelancers win projects. Generate premium, high-converting proposals in seconds with ProposeAI.
                    </p>
                    <div style="display: flex; gap: 16px;">
                        <a href="#" style="width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 8px; color: var(--fg-secondary); transition: all 0.3s;" onmouseover="this.style.color='var(--accent-primary)';this.style.borderColor='var(--accent-primary)'" onmouseout="this.style.color='var(--fg-secondary)';this.style.borderColor='var(--glass-border)'">𝕏</a>
                        <a href="#" style="width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 8px; color: var(--fg-secondary); transition: all 0.3s;" onmouseover="this.style.color='var(--accent-primary)';this.style.borderColor='var(--accent-primary)'" onmouseout="this.style.color='var(--fg-secondary)';this.style.borderColor='var(--glass-border)'">in</a>
                        <a href="#" style="width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 8px; color: var(--fg-secondary); transition: all 0.3s;" onmouseover="this.style.color='var(--accent-primary)';this.style.borderColor='var(--accent-primary)'" onmouseout="this.style.color='var(--fg-secondary)';this.style.borderColor='var(--glass-border)'">📫</a>
                    </div>
                </div>

                <!-- Column 2: Services -->
                <div>
                    <h4 style="font-family: 'Space Grotesk', sans-serif; font-size: 1rem; font-weight: 700; color: var(--fg-primary); margin-bottom: 24px;">Services</h4>
                    <ul style="list-style: none; display: flex; flex-direction: column; gap: 12px;">
                        <li><a href="#hero" style="font-size: 0.9rem; color: var(--fg-muted); text-decoration: none; transition: all 0.2s;" onmouseover="this.style.color='var(--accent-primary)';this.style.transform='translateX(4px)'" onmouseout="this.style.color='var(--fg-muted)';this.style.transform=''">AI Proposal Generation</a></li>
                        <li><a href="#templates" style="font-size: 0.9rem; color: var(--fg-muted); text-decoration: none; transition: all 0.2s;" onmouseover="this.style.color='var(--accent-primary)';this.style.transform='translateX(4px)'" onmouseout="this.style.color='var(--fg-muted)';this.style.transform=''">Professional Templates</a></li>
                        <li><a href="#features" style="font-size: 0.9rem; color: var(--fg-muted); text-decoration: none; transition: all 0.2s;" onmouseover="this.style.color='var(--accent-primary)';this.style.transform='translateX(4px)'" onmouseout="this.style.color='var(--fg-muted)';this.style.transform=''">Project Analytics</a></li>
                        <li><a href="#pricing" style="font-size: 0.9rem; color: var(--fg-muted); text-decoration: none; transition: all 0.2s;" onmouseover="this.style.color='var(--accent-primary)';this.style.transform='translateX(4px)'" onmouseout="this.style.color='var(--fg-muted)';this.style.transform=''">Pro Subscriptions</a></li>
                    </ul>
                </div>

                <!-- Column 3: Company -->
                <div>
                    <h4 style="font-family: 'Space Grotesk', sans-serif; font-size: 1rem; font-weight: 700; color: var(--fg-primary); margin-bottom: 24px;">Company</h4>
                    <ul style="list-style: none; display: flex; flex-direction: column; gap: 12px;">
                        <li><a href="#" style="font-size: 0.9rem; color: var(--fg-muted); text-decoration: none; transition: all 0.2s;" onmouseover="this.style.color='var(--accent-primary)';this.style.transform='translateX(4px)'" onmouseout="this.style.color='var(--fg-muted)';this.style.transform=''">About Us</a></li>
                        <li><a href="#" style="font-size: 0.9rem; color: var(--fg-muted); text-decoration: none; transition: all 0.2s;" onmouseover="this.style.color='var(--accent-primary)';this.style.transform='translateX(4px)'" onmouseout="this.style.color='var(--fg-muted)';this.style.transform=''">Our Mission</a></li>
                        <li><a href="#" style="font-size: 0.9rem; color: var(--fg-muted); text-decoration: none; transition: all 0.2s;" onmouseover="this.style.color='var(--accent-primary)';this.style.transform='translateX(4px)'" onmouseout="this.style.color='var(--fg-muted)';this.style.transform=''">Privacy Policy</a></li>
                        <li><a href="#" style="font-size: 0.9rem; color: var(--fg-muted); text-decoration: none; transition: all 0.2s;" onmouseover="this.style.color='var(--accent-primary)';this.style.transform='translateX(4px)'" onmouseout="this.style.color='var(--fg-muted)';this.style.transform=''">Terms of Service</a></li>
                    </ul>
                </div>

                <!-- Column 4: Support -->
                <div>
                    <h4 style="font-family: 'Space Grotesk', sans-serif; font-size: 1rem; font-weight: 700; color: var(--fg-primary); margin-bottom: 24px;">Support</h4>
                    <ul style="list-style: none; display: flex; flex-direction: column; gap: 12px;">
                        <li><a href="mailto:support@proposeai.com" style="font-size: 0.9rem; color: var(--fg-muted); text-decoration: none; transition: all 0.2s;" onmouseover="this.style.color='var(--accent-primary)';this.style.transform='translateX(4px)'" onmouseout="this.style.color='var(--fg-muted)';this.style.transform=''">Contact Support</a></li>
                        <li><a href="#" style="font-size: 0.9rem; color: var(--fg-muted); text-decoration: none; transition: all 0.2s;" onmouseover="this.style.color='var(--accent-primary)';this.style.transform='translateX(4px)'" onmouseout="this.style.color='var(--fg-muted)';this.style.transform=''">Help Center</a></li>
                        <li><a href="#" style="font-size: 0.9rem; color: var(--fg-muted); text-decoration: none; transition: all 0.2s;" onmouseover="this.style.color='var(--accent-primary)';this.style.transform='translateX(4px)'" onmouseout="this.style.color='var(--fg-muted)';this.style.transform=''">Live Chat</a></li>
                        <li><a href="#" style="font-size: 0.9rem; color: var(--fg-muted); text-decoration: none; transition: all 0.2s;" onmouseover="this.style.color='var(--accent-primary)';this.style.transform='translateX(4px)'" onmouseout="this.style.color='var(--fg-muted)';this.style.transform=''">Affiliate Program</a></li>
                    </ul>
                </div>
            </div>

            <!-- Bottom Line -->
            <div class="reveal" style="max-width: 1400px; margin: 0 auto; display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; padding-top: 32px; border-top: 1px solid var(--glass-border);">
                <p style="font-size: 0.85rem; color: var(--fg-muted);">
                    © 2026 ProposeAI. Designed & Developed for the future of freelancing.
                </p>
                <div style="display: flex; gap: 24px; margin-top: 12px;">
                    <span style="font-size: 0.8rem; color: var(--fg-secondary); display: flex; align-items: center; gap: 6px;">
                        <span style="width: 8px; height: 8px; background: #00ff88; border-radius: 50%; display: inline-block;"></span>
                        System Operational
                    </span>
                    <span style="font-size: 0.8rem; color: var(--fg-muted);">India / Global</span>
                </div>
            </div>
        </footer>
    </main>


    <!-- Send Proposal Modal -->
    <div class="sidebar-overlay" id="sendModalOverlay" style="z-index: 200;"></div>
    <div id="sendModal" class="glass-card stagger-1" style="display: none; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 90%; max-width: 400px; z-index: 201; padding: 32px; flex-direction: column; gap: 20px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
            <h3 style="font-size: 1.25rem; font-weight: 700; color: var(--fg-primary);">Send Proposal</h3>
            <button id="closeSendModal" style="background: none; border: none; color: var(--fg-muted); cursor: pointer;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
            </button>
        </div>
        <form id="sendProposalForm" style="display: flex; flex-direction: column; gap: 16px;">
            <div class="form-group" style="margin-bottom: 0;">
                <label for="recipientInput" class="form-label">Client Email or Phone Number</label>
                <input type="text" id="recipientInput" class="form-input" placeholder="client@example.com or +1234567890" required>
            </div>
            <div class="form-group" style="margin-bottom: 0;">
                <label for="authPassword" class="form-label">Your Password</label>
                <input type="password" id="authPassword" class="form-input" placeholder="Enter your password to verify" required>
            </div>
            <button type="submit" class="btn-generate" id="confirmSendBtn" style="padding: 14px; margin-top: 8px;">
                <span class="btn-text" id="confirmSendText">Send Now</span>
                <span class="btn-loader" id="confirmSendLoader" aria-hidden="true" style="display: none; position: static; margin: 0 auto;"></span>
            </button>
        </form>
    </div>

    <!-- Loading Overlay -->
    <div class="loading-overlay" id="loadingOverlay" role="alert" aria-live="polite" aria-label="Generating proposal">
        <div class="loading-animation">
            <div class="loading-bar"></div>
        </div>
        <div class="loading-text">Generating your premium proposal...</div>
    </div>

    <!-- Toast Container -->
    <div class="toast-container" id="toastContainer" role="status" aria-live="polite"></div>

    <script>
        // --- Ultra Smooth Loader ---
        window.addEventListener('load', () => {
            const loader = document.getElementById('page-loader');
            if (loader) {
                setTimeout(() => {
                    loader.classList.add('finish');
                    setTimeout(() => {
                        loader.style.display = 'none';
                        initPremiumInteractions();
                    }, 1200);
                }, 500);
            } else {
                initPremiumInteractions();
            }
        });

        function initPremiumInteractions() {
            const reveals = document.querySelectorAll('.reveal');
            
            // Stagger entrance for above-the-fold reveals
            reveals.forEach((el, index) => {
                if (el.getBoundingClientRect().top < window.innerHeight) {
                    setTimeout(() => {
                        el.classList.add('active');
                    }, 150 + (index * 150));
                }
            });

            // Scroll Reveals for the rest
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        setTimeout(() => {
                            entry.target.classList.add('active');
                        }, 100);
                        observer.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.1, rootMargin: "0px 0px -50px 0px" });
            
            reveals.forEach(el => observer.observe(el));

"""

final_content = top_part + recovered_text + bottom_part

with open(file_path, "w", encoding="utf-8") as f:
    f.write(final_content)

print("Recovered index.html successfully.")
