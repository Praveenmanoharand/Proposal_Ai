import re

# 1. Update welcome.html
welcome_path = r"g:\Proposal\templates\welcome.html"
with open(welcome_path, "r", encoding="utf-8") as f:
    welcome_content = f.read()

# The block to remove starts precisely with <!-- Feedback / Testimonials Section -->
# and continues up to <!-- Contact Section -->
pattern = re.compile(r'(\s*<!-- Feedback / Testimonials Section -->.*?)(?=\s*<!-- Contact Section -->)', re.DOTALL)
welcome_content_new = pattern.sub('', welcome_content)

with open(welcome_path, "w", encoding="utf-8") as f:
    f.write(welcome_content_new)
print("Removed fake reviews from welcome.html")


# 2. Update index.html
index_path = r"g:\Proposal\templates\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    index_content = f.read()

contact_html = """
        <!-- ============================
             CONTACT SECTION
             ============================ -->
        <section id="contact" style="padding:100px 40px;max-width:1400px;margin:0 auto;">
            <div class="reveal" style="text-align:center;margin-bottom:64px;">
                <h2 style="font-family:'Space Grotesk',sans-serif;font-size:clamp(1.8rem,4vw,3rem);font-weight:700;line-height:1.1;margin-bottom:16px;">
                    Let's Connect
                </h2>
                <p style="font-size:1.1rem;color:var(--fg-secondary);max-width:540px;margin:0 auto;">
                    Have questions about our enterprise plans, need custom integrations, or just want to say hi?
                </p>
            </div>
            
            <div class="glass-card reveal" style="padding:40px; max-width: 900px; margin: 0 auto; display: flex; flex-wrap: wrap; gap: 40px;">
                <!-- Left side (Info) -->
                <div style="flex: 1; min-width: 300px;">
                    <h3 style="font-size: 1.5rem; font-weight: 700; margin-bottom: 24px; color: var(--fg-primary);">Contact Information</h3>
                    <div style="display: flex; gap: 16px; margin-bottom: 24px; align-items: center;">
                        <div style="width: 48px; height: 48px; border-radius: 50%; background: var(--glass-bg); border: 1px solid var(--glass-border); display: flex; align-items: center; justify-content: center; color: var(--accent-primary);">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                        </div>
                        <div>
                            <p style="font-weight: 700; margin: 0;">Email Us</p>
                            <p style="color: var(--fg-secondary); font-size: 0.9rem; margin: 0;">hello@proposeai.com</p>
                        </div>
                    </div>
                    <div style="display: flex; gap: 16px; align-items: center;">
                        <div style="width: 48px; height: 48px; border-radius: 50%; background: var(--glass-bg); border: 1px solid var(--glass-border); display: flex; align-items: center; justify-content: center; color: var(--accent-primary);">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                        </div>
                        <div>
                            <p style="font-weight: 700; margin: 0;">Location</p>
                            <p style="color: var(--fg-secondary); font-size: 0.9rem; margin: 0;">Global / Remote</p>
                        </div>
                    </div>
                </div>
                
                <!-- Right side (Form) -->
                <div style="flex: 1.5; min-width: 300px;">
                    <form style="display: flex; flex-direction: column; gap: 16px;">
                        <div style="display: flex; gap: 16px; flex-wrap: wrap;">
                            <div style="flex: 1; min-width: 140px;">
                                <label style="display: block; font-size: 0.85rem; color: var(--fg-secondary); margin-bottom: 6px;">First Name</label>
                                <input type="text" style="width: 100%; background: rgba(0,0,0,0.3); border: 1px solid var(--glass-border); border-radius: 8px; padding: 12px; color: var(--fg-primary); outline: none; transition: border-color 0.3s;" onfocus="this.style.borderColor='var(--accent-primary)'" onblur="this.style.borderColor='var(--glass-border)'" placeholder="John">
                            </div>
                            <div style="flex: 1; min-width: 140px;">
                                <label style="display: block; font-size: 0.85rem; color: var(--fg-secondary); margin-bottom: 6px;">Last Name</label>
                                <input type="text" style="width: 100%; background: rgba(0,0,0,0.3); border: 1px solid var(--glass-border); border-radius: 8px; padding: 12px; color: var(--fg-primary); outline: none; transition: border-color 0.3s;" onfocus="this.style.borderColor='var(--accent-primary)'" onblur="this.style.borderColor='var(--glass-border)'" placeholder="Doe">
                            </div>
                        </div>
                        <div>
                            <label style="display: block; font-size: 0.85rem; color: var(--fg-secondary); margin-bottom: 6px;">Work Email</label>
                            <input type="email" style="width: 100%; background: rgba(0,0,0,0.3); border: 1px solid var(--glass-border); border-radius: 8px; padding: 12px; color: var(--fg-primary); outline: none; transition: border-color 0.3s;" onfocus="this.style.borderColor='var(--accent-primary)'" onblur="this.style.borderColor='var(--glass-border)'" placeholder="john@company.com">
                        </div>
                        <div>
                            <label style="display: block; font-size: 0.85rem; color: var(--fg-secondary); margin-bottom: 6px;">Message</label>
                            <textarea rows="4" style="width: 100%; background: rgba(0,0,0,0.3); border: 1px solid var(--glass-border); border-radius: 8px; padding: 12px; color: var(--fg-primary); outline: none; transition: border-color 0.3s;" onfocus="this.style.borderColor='var(--accent-primary)'" onblur="this.style.borderColor='var(--glass-border)'" placeholder="How can we help?"></textarea>
                        </div>
                        <button type="button" class="btn-generate" style="padding: 14px; margin-top: 8px;">
                            <span class="btn-text" style="position:relative;z-index:2;">Send Message</span>
                        </button>
                    </form>
                </div>
            </div>
        </section>

        <!-- Detailed Footer -->"""

if "<!-- Detailed Footer -->" in index_content and "CONTACT SECTION" not in index_content:
    index_content_new = index_content.replace("        <!-- Detailed Footer -->", contact_html)
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(index_content_new)
    print("Injected contact section into index.html")
else:
    print("Could not inject into index.html or already exists")
