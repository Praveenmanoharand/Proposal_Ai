import re

print("Fixing all issues in index.html and main.js...")

# ============================================================
# FIX 1: index.html — Orphaned parallax JS (syntax error)
# ============================================================
index_path = r"g:\Proposal\templates\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    index = f.read()

broken = """            reveals.forEach(el => observer.observe(el));

                const centerY = window.innerHeight / 2;
                orbs.forEach(orb => {
                    const speed = parseFloat(orb.dataset.speed);
                    orb.style.transform = `translate(${(clientX - centerX) * speed / 100}px, ${(clientY - centerY) * speed / 100}px)`;
                });
            });

            // 3D Tilt"""

fixed = """            reveals.forEach(el => observer.observe(el));

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

if broken in index:
    index = index.replace(broken, fixed)
    print("  [OK] Fixed orphaned parallax JS syntax error in index.html")
else:
    print("  [SKIP] Parallax fix already applied or pattern not found")

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index)


# ============================================================
# FIX 2: main.js — Missing updateUIForPlan function
# ============================================================
main_js_path = r"g:\Proposal\static\js\main.js"
with open(main_js_path, "r", encoding="utf-8") as f:
    main_js = f.read()

if "function updateUIForPlan" not in main_js:
    insert_before = """// ================================
// LOAD USER PLAN STATUS
// ================================
async function loadUserStatus() {"""

    new_block = """// ================================
// UPDATE UI FOR PLAN
// ================================
function updateUIForPlan() {
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
async function loadUserStatus() {"""

    if insert_before in main_js:
        main_js = main_js.replace(insert_before, new_block)
        print("  [OK] Added missing updateUIForPlan function to main.js")
    else:
        print("  [ERROR] Could not find insertion point in main.js")
else:
    print("  [SKIP] updateUIForPlan already exists in main.js")

with open(main_js_path, "w", encoding="utf-8") as f:
    f.write(main_js)

print("\nAll fixes applied!")
