"""
Base Page Object Model class for common page functionality
"""
from playwright.sync_api import Page
import os
from datetime import datetime


from utils.test_utils import SCREENSHOTS_DIR

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.screenshot_dir = SCREENSHOTS_DIR
        
    def navigate_to(self, url: str):
        """Navigate to a specific URL"""
        self.page.goto(url)
        
    def click_element(self, selector: str):
        """Click on an element"""
        self.page.click(selector)
        
    def fill_input(self, selector: str, value: str):
        """Fill an input field"""
        self.page.fill(selector, value)
        
    def select_option(self, selector: str, value: str):
        """Select an option from dropdown"""
        self.page.select_option(selector, value)
        
    def take_screenshot(self, name: str):
        """Take a screenshot"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}.png"
        filepath = os.path.join(self.screenshot_dir, filename)
        os.makedirs(self.screenshot_dir, exist_ok=True)
        self.page.screenshot(path=filepath)
        return filepath
        
    def get_text(self, selector: str) -> str:
        """Get text from an element"""
        return self.page.text_content(selector)
        
    def is_visible(self, selector: str) -> bool:
        """Check if element is visible"""
        return self.page.is_visible(selector)
        
    def wait_for_element(self, selector: str, timeout: int = 5000):
        """Wait for element to be visible"""
        self.page.wait_for_selector(selector, timeout=timeout)
