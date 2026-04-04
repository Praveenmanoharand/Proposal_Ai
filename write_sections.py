import sys

file_path = r"g:\Proposal\templates\welcome.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

target = """    </main>

    <footer class="border-t border-white/10 py-10 bg-black/50 backdrop-blur-xl">
        <div class="max-w-[1400px] mx-auto px-6 md:px-12 flex flex-col md:flex-row justify-between items-center text-sm text-gray-500">
            <div>&copy; 2026 ProposeAI. Intelligence Redefined.</div>
            <div class="mt-4 md:mt-0 flex gap-6">
                <a href="#" class="hover:text-white transition-colors">Privacy</a>
                <a href="#" class="hover:text-white transition-colors">Terms</a>
                <a href="#" class="hover:text-white transition-colors">Contact</a>
            </div>
        </div>
    </footer>"""

new_sections = """        <!-- Feedback / Testimonials Section -->
        <section id="feedback" class="mb-32">
            <div class="text-center mb-16 reveal">
                <h2 class="text-4xl md:text-5xl font-['Space_Grotesk'] font-bold mb-4">What Our Users Say</h2>
                <p class="text-gray-400 text-lg font-light max-w-2xl mx-auto">
                    Freelancers and agencies worldwide are winning more high-value clients with ProposeAI.
                </p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- Review 1 -->
                <div class="glass-card p-8 reveal stagger-1">
                    <div class="flex items-center gap-4 mb-6">
                        <div class="w-12 h-12 rounded-full bg-gradient-to-br from-purple-500 to-cyan-500 flex items-center justify-center text-white font-bold text-xl">S</div>
                        <div>
                            <h4 class="font-bold text-lg">Sarah Jenkins</h4>
                            <p class="text-gray-400 text-sm">UI/UX Designer</p>
                        </div>
                    </div>
                    <div class="text-cyan-400 mb-4 flex gap-1">
                        <svg width="16" height="16" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                        <svg width="16" height="16" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                        <svg width="16" height="16" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                        <svg width="16" height="16" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                        <svg width="16" height="16" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                    </div>
                    <p class="text-gray-300 leading-relaxed font-light">"Before ProposeAI, I spent hours assembling PDFs. Now, I enter 3 lines of requirements and my clients receive a legally-sound, breathtaking proposal. My close rate doubled in a month."</p>
                </div>
                
                <!-- Review 2 -->
                <div class="glass-card p-8 reveal stagger-2 relative overflow-hidden">
                    <div class="absolute inset-0 bg-gradient-to-br from-purple-900/10 to-transparent"></div>
                    <div class="relative z-10">
                        <div class="flex items-center gap-4 mb-6">
                            <div class="w-12 h-12 rounded-full bg-gradient-to-br from-blue-500 to-indigo-500 flex items-center justify-center text-white font-bold text-xl">M</div>
                            <div>
                                <h4 class="font-bold text-lg">Michael Chen</h4>
                                <p class="text-gray-400 text-sm">Full Stack Developer</p>
                            </div>
                        </div>
                        <div class="text-cyan-400 mb-4 flex gap-1">
                            <svg width="16" height="16" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                            <svg width="16" height="16" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                            <svg width="16" height="16" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                            <svg width="16" height="16" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                            <svg width="16" height="16" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                        </div>
                        <p class="text-gray-300 leading-relaxed font-light">"The multi-currency support is a gamechanger. I pitch to clients in the US and UK effortlessly. The generated PDFs look like they were made by a top-tier agency."</p>
                    </div>
                </div>

                <!-- Review 3 -->
                <div class="glass-card p-8 reveal stagger-3">
                    <div class="flex items-center gap-4 mb-6">
                        <div class="w-12 h-12 rounded-full bg-gradient-to-br from-pink-500 to-orange-400 flex items-center justify-center text-white font-bold text-xl">A</div>
                        <div>
                            <h4 class="font-bold text-lg">Alex Rivera</h4>
                            <p class="text-gray-400 text-sm">Marketing Consultant</p>
                        </div>
                    </div>
                    <div class="text-cyan-400 mb-4 flex gap-1">
                        <svg width="16" height="16" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                        <svg width="16" height="16" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                        <svg width="16" height="16" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                        <svg width="16" height="16" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                        <svg width="16" height="16" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                    </div>
                    <p class="text-gray-300 leading-relaxed font-light">"The proposal history helps me keep track of all my leads, and the AI's milestone breakdowns are surprisingly accurate. Best investment for my freelance business."</p>
                </div>
            </div>
        </section>

        <!-- Contact Section -->
        <section id="contact" class="mb-20">
            <div class="glass-card p-10 md:p-16 reveal border-t border-purple-500/20">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-16">
                    <div>
                        <h2 class="text-4xl font-['Space_Grotesk'] font-bold mb-6">Let's Connect</h2>
                        <p class="text-gray-400 text-lg mb-10 font-light">
                            Have questions about our enterprise plans, need custom integrations, or just want to say hi? Our team is always ready to assist you.
                        </p>
                        
                        <div class="space-y-6">
                            <div class="flex items-center gap-4 text-gray-300">
                                <div class="w-12 h-12 rounded-full bg-white/5 flex items-center justify-center border border-white/10 text-cyan-400">
                                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                                </div>
                                <div>
                                    <p class="font-bold text-white">Email Us</p>
                                    <p class="text-sm font-light">hello@proposeai.com</p>
                                </div>
                            </div>
                            <div class="flex items-center gap-4 text-gray-300">
                                <div class="w-12 h-12 rounded-full bg-white/5 flex items-center justify-center border border-white/10 text-cyan-400">
                                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                                </div>
                                <div>
                                    <p class="font-bold text-white">Location</p>
                                    <p class="text-sm font-light">Global / Remote</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div>
                        <form class="space-y-4">
                            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                                <div>
                                    <label class="block text-sm text-gray-400 mb-1" for="name">First Name</label>
                                    <input type="text" id="name" class="w-full bg-black/40 border border-white/10 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-purple-500 transition-colors" placeholder="John">
                                </div>
                                <div>
                                    <label class="block text-sm text-gray-400 mb-1" for="lastname">Last Name</label>
                                    <input type="text" id="lastname" class="w-full bg-black/40 border border-white/10 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-purple-500 transition-colors" placeholder="Doe">
                                </div>
                            </div>
                            <div>
                                <label class="block text-sm text-gray-400 mb-1" for="email">Work Email</label>
                                <input type="email" id="email" class="w-full bg-black/40 border border-white/10 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-purple-500 transition-colors" placeholder="john@company.com">
                            </div>
                            <div>
                                <label class="block text-sm text-gray-400 mb-1" for="message">Message</label>
                                <textarea id="message" rows="4" class="w-full bg-black/40 border border-white/10 rounded-lg px-4 py-3 text-white focus:outline-none focus:border-purple-500 transition-colors" placeholder="How can we help?"></textarea>
                            </div>
                            <button type="button" class="w-full bg-gradient-to-r from-purple-600 to-cyan-600 text-white font-bold py-4 rounded-lg hover:opacity-90 transition-opacity">
                                Send Message
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </section>

    </main>

    <!-- Expanded Footer Section -->
    <footer class="border-t border-white/10 pt-20 pb-10 bg-black/80 backdrop-blur-2xl relative overflow-hidden">
        <div class="absolute top-0 left-1/2 -translate-x-1/2 w-3/4 h-[1px] bg-gradient-to-r from-transparent via-purple-500/50 to-transparent"></div>
        <div class="max-w-[1400px] mx-auto px-6 md:px-12">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-12 mb-16">
                <div class="md:col-span-1">
                    <a href="/" class="flex items-center gap-2 mb-6" style="text-decoration:none;color:inherit;">
                        <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-purple-500 to-cyan-500 flex items-center justify-center">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"/><polyline points="14 2 14 8 20 8"/></svg>
                        </div>
                        <span class="font-bold text-xl tracking-wide">ProposeAI</span>
                    </a>
                    <p class="text-gray-400 font-light text-sm leading-relaxed pr-4">
                        Stop losing clients to amateur proposals. Let our sophisticated AI engine generate premium, legally-sound proposals in flat 90 seconds. 
                    </p>
                </div>
                
                <div>
                    <h5 class="text-white font-bold mb-4">Product</h5>
                    <ul class="space-y-3 text-gray-400 text-sm font-light">
                        <li><a href="#features" class="hover:text-cyan-400 transition-colors">Features</a></li>
                        <li><a href="#pricing" class="hover:text-cyan-400 transition-colors">Pricing</a></li>
                        <li><a href="#templates" class="hover:text-cyan-400 transition-colors">Templates</a></li>
                        <li><a href="#feedback" class="hover:text-cyan-400 transition-colors">Testimonials</a></li>
                    </ul>
                </div>

                <div>
                    <h5 class="text-white font-bold mb-4">Resources</h5>
                    <ul class="space-y-3 text-gray-400 text-sm font-light">
                        <li><a href="#" class="hover:text-cyan-400 transition-colors">Blog</a></li>
                        <li><a href="#" class="hover:text-cyan-400 transition-colors">Help Center</a></li>
                        <li><a href="#" class="hover:text-cyan-400 transition-colors">Freelance Guide</a></li>
                        <li><a href="#" class="hover:text-cyan-400 transition-colors">API Documentation</a></li>
                    </ul>
                </div>

                <div>
                    <h5 class="text-white font-bold mb-4">Company</h5>
                    <ul class="space-y-3 text-gray-400 text-sm font-light">
                        <li><a href="#" class="hover:text-cyan-400 transition-colors">About Us</a></li>
                        <li><a href="#" class="hover:text-cyan-400 transition-colors">Careers</a></li>
                        <li><a href="#" class="hover:text-cyan-400 transition-colors">Privacy Policy</a></li>
                        <li><a href="#" class="hover:text-cyan-400 transition-colors">Terms of Service</a></li>
                    </ul>
                </div>
            </div>
            
            <div class="pt-8 border-t border-white/5 flex flex-col md:flex-row justify-between items-center gap-4 text-xs text-gray-500 font-light">
                <p>&copy; 2026 ProposeAI. Designed & Developed for the future of freelancing.</p>
                <div class="flex items-center gap-2">
                    <span class="w-2 h-2 rounded-full bg-green-500 animate-pulse"></span>
                    Systems Operational
                </div>
            </div>
        </div>
    </footer>"""

if target in content:
    content = content.replace(target, new_sections)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Injection successful.")
else:
    print("Target block not found. Could not inject.")
