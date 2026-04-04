import re

# ---- 1. Revert main.js (remove updateUIForPlan function) ----
main_js_path = r"g:\Proposal\static\js\main.js"
with open(main_js_path, "r", encoding="utf-8") as f:
    main_js = f.read()

block_to_remove = """// ================================
// UPDATE UI FOR PLAN
// ================================
function updateUIForPlan() {
    const plan = state.userPlan || 'free';
    
    // Inject plan badge into nav
    injectPlanBadge();
    
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
"""
replacement = """// ================================
// LOAD USER PLAN STATUS
// ================================
"""
main_js = main_js.replace(block_to_remove, replacement)
with open(main_js_path, "w", encoding="utf-8") as f:
    f.write(main_js)
print("1. Reverted main.js (removed updateUIForPlan)")

# ---- 2. Revert index.html contact section ----
index_path = r"g:\Proposal\templates\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    index = f.read()

# Remove contact section injected between templates section and footer
contact_pattern = re.compile(
    r'\s*<!-- ============================\s*\n\s*CONTACT SECTION\s*\n\s*============================.*?<!-- Detailed Footer -->',
    re.DOTALL
)
index = contact_pattern.sub('\n        <!-- Detailed Footer -->', index)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index)
print("2. Reverted index.html (removed contact section)")

# ---- 3. Revert parallax JS fix in index.html ----
with open(index_path, "r", encoding="utf-8") as f:
    index = f.read()

fixed_parallax = """            reveals.forEach(el => observer.observe(el));

            // Parallax Orbs
            const orbs = document.querySelectorAll('.orb-js');
            document.addEventListener('mousemove', (e) => {
                const { clientX, clientY } = e;
                const centerX = window.innerWidth / 2;
                const centerY = window.innerHeight / 2;
                orbs.forEach(orb => {
                    const speed = parseFloat(orb.dataset.speed) || 0;
                    orb.style.transform = `translate(${(clientX - centerX) * speed / 100}px, ${(clientY - centerY) * speed / 100}px)`;
                });
            });

            // 3D Tilt"""

original_parallax = """            reveals.forEach(el => observer.observe(el));

                const centerY = window.innerHeight / 2;
                orbs.forEach(orb => {
                    const speed = parseFloat(orb.dataset.speed);
                    orb.style.transform = `translate(${(clientX - centerX) * speed / 100}px, ${(clientY - centerY) * speed / 100}px)`;
                });
            });

            // 3D Tilt"""

index = index.replace(fixed_parallax, original_parallax)
with open(index_path, "w", encoding="utf-8") as f:
    f.write(index)
print("3. Reverted index.html parallax JS fix")
