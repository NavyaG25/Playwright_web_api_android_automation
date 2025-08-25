import pytest
import asyncio
from playwright.async_api import async_playwright, Page
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.logger import log_info, log_error
from utils.waits import wait_for_selector, short_wait
from utils.screenshots import take_screenshot
from config import settings

@pytest.mark.asyncio
async def test_login_mobile():
    log_info("Starting mobile login test on SauceDemo")
    async with async_playwright() as p:
        test_steps = []
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        try:
            if settings.ANDROID_CDP:
                log_info("[MODE] Running on REAL ANDROID DEVICE via Chrome DevTools Protocol (CDP)")
                log_info("Connecting to Chrome on Android device via CDP...")
                browser = await p.chromium.connect_over_cdp(f"http://{settings.CDP_HOST}:{settings.CDP_PORT}")
                log_info("Connected to device. Getting context and page...")
                context = browser.contexts[0] if browser.contexts else await browser.new_context()
                pages = context.pages
                if not pages:
                    page = await context.new_page()
                else:
                    page = pages[0]
                await short_wait(0.8)
                log_info("Navigating to SauceDemo URL in Chrome tab on REAL DEVICE...")
                await page.goto(settings.URL)
                await short_wait(1.0)
                ua = await page.evaluate("navigator.userAgent")
                log_info(f"[REAL DEVICE] User agent: {ua}")
                log_info(f"[REAL DEVICE] Current page URL: {page.url}")
                log_info(f"[REAL DEVICE] Page title: {await page.title()}")
                test_steps.append({"step": "connect_cdp", "status": "passed", "details": f"User agent: {ua}"})
            else:
                log_info("[MODE] Running in PIXEL 3 (or configured) MOBILE EMULATION mode")
                device = p.devices[settings.DEVICE]
                log_info(f"[EMULATION] Device descriptor: {device}")
                browser = await p.chromium.launch(headless=settings.HEADLESS)
                context = await browser.new_context(
                    user_agent=device["user_agent"],
                    viewport=device["viewport"],
                    is_mobile=device.get("is_mobile", True),
                    has_touch=device.get("has_touch", True),
                    device_scale_factor=device.get("device_scale_factor", 2.625),
                    locale=device.get("locale", "en-US")
                )
                page = await context.new_page()
                log_info("Navigating to SauceDemo URL in emulated browser...")
                await page.goto(settings.URL)
                await short_wait(1.0)
                ua = await page.evaluate("navigator.userAgent")
                log_info(f"[EMULATION] User agent: {ua}")
                log_info(f"[EMULATION] Current page URL: {page.url}")
                log_info(f"[EMULATION] Page title: {await page.title()}")
                test_steps.append({"step": "emulate_device", "status": "passed", "details": f"User agent: {ua}"})

            homepage_screenshot_name = f"saucedemo_homepage_mobile_{timestamp}"
            homepage_screenshot_path = await take_screenshot(page, homepage_screenshot_name)
            log_info(f"SauceDemo homepage screenshot after navigation: {homepage_screenshot_path}")
            login_page = LoginPage(page)
            log_info("Waiting for username field...")
            await wait_for_selector(page, login_page.USERNAME_INPUT, timeout=15000)
            log_info("Entering username...")
            await login_page.enter_username("standard_user")
            log_info("Entering password...")
            await login_page.enter_password("secret_sauce")
            log_info("Clicking login button...")
            await login_page.click_login()
            log_info("Waiting for Products page...")
            await wait_for_selector(page, login_page.PRODUCTS_TEXT)
            products_page = ProductsPage(page)
            assert await products_page.is_loaded(), "Products page not loaded!"
            test_steps.append({"step": "login", "status": "passed", "details": "Login successful, Products page loaded."})
            login_screenshot_name = f"saucedemo_login_mobile_{timestamp}"
            login_screenshot_path = await take_screenshot(page, login_screenshot_name)
            log_info(f"Login screenshot after successful login: {login_screenshot_path}")
            result = {
                "test": "test_login_mobile",
                "status": "passed",
                "steps": test_steps,
                "screenshot": homepage_screenshot_path,
                "login_screenshot": login_screenshot_path
            }
        except Exception as e:
            log_error(f"Test failed: {e}")
            test_steps.append({"step": "error", "status": "failed", "details": str(e)})
            result = {"test": "test_login_mobile", "status": "failed", "steps": test_steps}
            raise
        finally:
            from utils.report import save_json_report
            from utils.html_report import generate_html_report
            json_name = f"login_test_result_{timestamp}"
            json_path = save_json_report(result, name=json_name)
            log_info(f"Test result JSON saved: {json_path}")
            html_path = generate_html_report(json_path)
            log_info(f"HTML report generated: {html_path}")
            await context.close()
            await browser.close()
