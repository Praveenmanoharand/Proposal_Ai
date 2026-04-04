import re

file_path = r"g:\Proposal\templates\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Revert CSS
css_old = """        .reveal {
            opacity: 0;
            transform: perspective(1500px) rotateX(-12deg) translateY(60px) scale(0.9);
            filter: blur(20px);
            transition: opacity 1.5s cubic-bezier(0.16, 1, 0.1, 1), 
                        transform 1.5s cubic-bezier(0.16, 1, 0.1, 1),
                        filter 1.5s cubic-bezier(0.16, 1, 0.1, 1);
            transform-origin: top center;
            will-change: transform, opacity, filter;
        }
        .reveal.active {
            opacity: 1;
            transform: perspective(1500px) rotateX(0deg) translateY(0) scale(1);
            filter: blur(0);
        }

    </style>"""
css_new = """        .reveal {
            opacity: 0;
            transform: perspective(1500px) rotateX(-12deg) translateY(60px) scale(0.9);
            filter: blur(20px);
            transition: opacity 1.5s cubic-bezier(0.16, 1, 0.1, 1), 
                        transform 1.5s cubic-bezier(0.16, 1, 0.1, 1),
                        filter 1.5s cubic-bezier(0.16, 1, 0.1, 1);
            transform-origin: top center;
            will-change: transform, opacity, filter;
        }

    </style>"""
content = content.replace(css_old, css_new)

# 2. Revert HTML loader
html_loader = """<body>
    <div id="page-loader">
        <div class="spinner"></div>
    </div>"""
content = content.replace(html_loader, "<body>\n    </div>")

# 3. Revert classes
content = content.replace('<nav class="nav-container reveal stagger-1"', '<nav class="nav-container"')
content = content.replace('<section class="hero-section reveal stagger-2"', '<section class="hero-section"')
content = content.replace('<div class="dashboard-grid reveal stagger-3"', '<div class="dashboard-grid"')
content = content.replace('<div class="metrics-strip reveal stagger-4"', '<div class="metrics-strip"')
content = content.replace('<div class="reveal" style="text-align:center;margin-bottom:64px;">', '<div style="text-align:center;margin-bottom:64px;">')

# remove all reveal and stagger classes in glass-cards
content = re.sub(r'class="glass-card reveal(?: stagger-\d)?"', 'class="glass-card"', content)
# remove stagger from sendModal
content = content.replace('id="sendModal" class="glass-card stagger-1"', 'id="sendModal" class="glass-card"')

# 4. Revert JS
js_old = """        // --- Ultra Smooth Loader ---
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
            
            reveals.forEach(el => observer.observe(el));"""
js_new = """        // --- Ultra Smooth Loader ---
        window.addEventListener('load', () => {
            const loader = document.getElementById('loader');
            setTimeout(() => {
                loader.style.opacity = '0';
                loader.style.visibility = 'hidden';
                loader.style.transform = 'scale(1.1)';
                initPremiumInteractions();
            }, 1000);
        });

        function initPremiumInteractions() {
            // Scroll Reveals
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) entry.target.classList.add('active');
                });
            }, { threshold: 0.1 });
            document.querySelectorAll('.reveal').forEach(el => observer.observe(el));"""

content = content.replace(js_old, js_new)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Reverted successfully.")
