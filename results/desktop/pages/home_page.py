"""
Home Page Object Model
"""
from .base_page import BasePage


class HomePage(BasePage):
    # Locators
    SIGNUP_LOGIN_BUTTON = "a[href='/login']"
    PRODUCTS_BUTTON = "a[href='/products']"
    HOME_TITLE = "title"
    LOGGED_IN_USER = ".navbar-nav li:last-child a"
    
    def __init__(self, page):
        super().__init__(page)
        
    def navigate_to_home(self):
        """Navigate to home page"""
        self.navigate_to("http://automationexercise.com")
        
    def click_signup_login(self):
        """Click on Signup/Login button"""
        self.click_element(self.SIGNUP_LOGIN_BUTTON)
        
    def click_products(self):
        """Click on Products button"""
        self.click_element(self.PRODUCTS_BUTTON)
        
    def is_home_page_visible(self) -> bool:
        """Verify home page is visible"""
        return "Automation Exercise" in self.page.title()
        
    def get_logged_in_user(self) -> str:
        """Get logged in user name"""
        try:
            return self.get_text(self.LOGGED_IN_USER)
        except:
            return ""
            
    def is_user_logged_in(self) -> bool:
        """Check if user is logged in"""
        return "Logged in as" in self.get_logged_in_user()
