import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()
        
        # 1. Capture Login Page
        print("Capturing login page...")
        await page.goto('http://127.0.0.1:5000/login')
        await page.wait_for_timeout(2000) # wait for animations
        await page.screenshot(path='static/images/login_screenshot.png', full_page=True)
        print("Login screenshot saved to static/images/login_screenshot.png")
        
        # 2. Register/Login to get session cookie
        print("Authenticating to access dashboard...")
        await page.evaluate('''async () => {
            await fetch('/api/register', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({name: 'AdminTest', email: 'admin_test@proposeai.com', password: 'password123'})
            });
            await fetch('/api/login', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({email: 'admin_test@proposeai.com', password: 'password123'})
            });
        }''')
        
        # 3. Capture Dashboard Page
        print("Capturing dashboard page...")
        await page.goto('http://127.0.0.1:5000/dashboard')
        # wait a bit for data to load and render animations
        await page.wait_for_timeout(3000)
        
        # force all reveals to be active and remove transitions so screenshots are crisp
        await page.evaluate('''() => {
            const loader = document.getElementById('page-loader');
            if (loader) loader.style.display = 'none';
            document.querySelectorAll('.reveal').forEach(el => {
                el.style.transition = 'none';
                el.classList.add('active');
                el.style.filter = 'none';
                el.style.opacity = '1';
                el.style.transform = 'none';
            });
        }''')
        await page.wait_for_timeout(500)
        
        await page.screenshot(path='static/images/index_screenshot.png', full_page=True)
        print("Dashboard screenshot saved to static/images/index_screenshot.png")
        
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
