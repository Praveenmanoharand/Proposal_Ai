import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()

        console_msgs = []
        js_errors = []
        page.on("console", lambda msg: console_msgs.append(f"[{msg.type}] {msg.text}"))
        page.on("pageerror", lambda err: js_errors.append(str(err)))

        # Login first
        await page.goto('http://127.0.0.1:5000/login')
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

        # Go to dashboard
        await page.goto('http://127.0.0.1:5000/dashboard')
        await page.wait_for_timeout(2000)

        print("=== JS ERRORS ===")
        for e in js_errors:
            print(e)

        print("\n=== CONSOLE MESSAGES ===")
        for m in console_msgs:
            print(m)

        # Check if body has content
        body_html = await page.evaluate("document.body.innerHTML.length")
        print(f"\nBody HTML length: {body_html}")

        nav = await page.query_selector('nav')
        print(f"Nav element found: {nav is not None}")

        # Check if things are visible
        main_el = await page.query_selector('main')
        print(f"Main element found: {main_el is not None}")
        if main_el:
            box = await main_el.bounding_box()
            print(f"Main bounding box: {box}")

        await page.screenshot(path='static/images/debug_screenshot.png')
        print("\nDebug screenshot saved.")

        await browser.close()

asyncio.run(main())
