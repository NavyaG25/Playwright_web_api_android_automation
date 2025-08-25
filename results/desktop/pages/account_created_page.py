"""
Account Created Page Object Model
"""
from .base_page import BasePage


class AccountCreatedPage(BasePage):
    # Locators
    ACCOUNT_CREATED_TEXT = "h2[data-qa='account-created']"
    CONTINUE_BUTTON = "a[data-qa='continue-button']"
    
    def __init__(self, page):
        super().__init__(page)
        
    def is_account_created_visible(self) -> bool:
        """Verify 'ACCOUNT CREATED!' is visible"""
        return self.is_visible(self.ACCOUNT_CREATED_TEXT)
        
    def click_continue(self):
        """Click continue button"""
        self.click_element(self.CONTINUE_BUTTON)
