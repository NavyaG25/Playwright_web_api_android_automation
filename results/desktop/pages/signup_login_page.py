"""
Signup/Login Page Object Model
"""
from .base_page import BasePage


class SignupLoginPage(BasePage):
    # Locators
    SIGNUP_NAME_INPUT = "input[data-qa='signup-name']"
    SIGNUP_EMAIL_INPUT = "input[data-qa='signup-email']"
    SIGNUP_BUTTON = "button[data-qa='signup-button']"
    NEW_USER_SIGNUP_TEXT = "h2:has-text('New User Signup!')"
    LOGIN_EMAIL_INPUT = "input[data-qa='login-email']"
    LOGIN_PASSWORD_INPUT = "input[data-qa='login-password']"
    LOGIN_BUTTON = "button[data-qa='login-button']"
    LOGIN_TO_ACCOUNT_TEXT = "h2:has-text('Login to your account')"
    
    def __init__(self, page):
        super().__init__(page)
        
    def is_new_user_signup_visible(self) -> bool:
        """Verify 'New User Signup!' is visible"""
        return self.is_visible(self.NEW_USER_SIGNUP_TEXT)
        
    def is_login_to_account_visible(self) -> bool:
        """Verify 'Login to your account' is visible"""
        return self.is_visible(self.LOGIN_TO_ACCOUNT_TEXT)
        
    def fill_signup_details(self, name: str, email: str):
        """Fill signup form details"""
        self.fill_input(self.SIGNUP_NAME_INPUT, name)
        self.fill_input(self.SIGNUP_EMAIL_INPUT, email)
        
    def click_signup_button(self):
        """Click signup button"""
        self.click_element(self.SIGNUP_BUTTON)
        
    def fill_login_details(self, email: str, password: str):
        """Fill login form details"""
        self.fill_input(self.LOGIN_EMAIL_INPUT, email)
        self.fill_input(self.LOGIN_PASSWORD_INPUT, password)
        
    def click_login_button(self):
        """Click login button"""
        self.click_element(self.LOGIN_BUTTON)
