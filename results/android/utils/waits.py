from playwright.async_api import Page
import asyncio
from typing import Optional

async def wait_for_selector(page: Page, selector: str, timeout: int = 5000):
    await page.wait_for_selector(selector, timeout=timeout)

async def short_wait(seconds: float = 0.7):
    await asyncio.sleep(seconds)
