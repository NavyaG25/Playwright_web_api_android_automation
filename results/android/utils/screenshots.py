from pathlib import Path
from playwright.async_api import Page
from datetime import datetime

SCREENSHOT_DIR = Path("screenshots")
SCREENSHOT_DIR.mkdir(exist_ok=True)

def get_screenshot_path(name: str) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return SCREENSHOT_DIR / f"{name}_{timestamp}.png"

async def take_screenshot(page: Page, name: str):
    path = get_screenshot_path(name)
    await page.screenshot(path=str(path), full_page=True)
    return str(path)
