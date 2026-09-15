import asyncio, os
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
        page = await browser.new_page()
        await page.goto("file://" + os.path.join(HERE, "valletta_instructor_outline.html"))
        await page.pdf(
            path=os.path.join(HERE, "valletta_instructor_outline.pdf"),
            width="8.5in",
            height="11in",
            print_background=True,
            margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
        )
        await browser.close()

asyncio.run(main())
