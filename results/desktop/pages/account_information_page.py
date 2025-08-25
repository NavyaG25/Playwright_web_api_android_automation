"""
Account Information Page Object Model
"""
from .base_page import BasePage


class AccountInformationPage(BasePage):
    # Locators
    TITLE_MR = "#id_gender1"
    TITLE_MRS = "#id_gender2"
    PASSWORD_INPUT = "#password"
    DAY_DROPDOWN = "#days"
    MONTH_DROPDOWN = "#months"
    YEAR_DROPDOWN = "#years"
    NEWSLETTER_CHECKBOX = "#newsletter"
    SPECIAL_OFFERS_CHECKBOX = "#optin"
    FIRST_NAME_INPUT = "#first_name"
    LAST_NAME_INPUT = "#last_name"
    COMPANY_INPUT = "#company"
    ADDRESS1_INPUT = "#address1"
    ADDRESS2_INPUT = "#address2"
    COUNTRY_DROPDOWN = "#country"
    STATE_INPUT = "#state"
    CITY_INPUT = "#city"
    ZIPCODE_INPUT = "#zipcode"
    MOBILE_NUMBER_INPUT = "#mobile_number"
    CREATE_ACCOUNT_BUTTON = "button[data-qa='create-account']"
    ENTER_ACCOUNT_INFO_TEXT = "h2:has-text('Enter Account Information')"
    
    def __init__(self, page):
        super().__init__(page)
        
    def is_enter_account_info_visible(self) -> bool:
        """Verify 'ENTER ACCOUNT INFORMATION' is visible"""
        return self.is_visible(self.ENTER_ACCOUNT_INFO_TEXT)
        
    def select_title(self, gender: str = "Mr"):
        """Select title (Mr/Mrs)"""
        if gender.lower() == "mr":
            self.click_element(self.TITLE_MR)
        else:
            self.click_element(self.TITLE_MRS)
            
    def fill_account_information(self, password: str, day: str, month: str, year: str):
        """Fill account information"""
        self.fill_input(self.PASSWORD_INPUT, password)
        self.select_option(self.DAY_DROPDOWN, day)
        self.select_option(self.MONTH_DROPDOWN, month)
        self.select_option(self.YEAR_DROPDOWN, year)
        
    def select_newsletter(self):
        """Select newsletter checkbox"""
        self.click_element(self.NEWSLETTER_CHECKBOX)
        
    def select_special_offers(self):
        """Select special offers checkbox"""
        self.click_element(self.SPECIAL_OFFERS_CHECKBOX)
        
    def fill_address_information(self, first_name: str, last_name: str, company: str,
                               address1: str, address2: str, country: str, state: str,
                               city: str, zipcode: str, mobile: str):
        """Fill address information"""
        self.fill_input(self.FIRST_NAME_INPUT, first_name)
        self.fill_input(self.LAST_NAME_INPUT, last_name)
        self.fill_input(self.COMPANY_INPUT, company)
        self.fill_input(self.ADDRESS1_INPUT, address1)
        self.fill_input(self.ADDRESS2_INPUT, address2)
        self.select_option(self.COUNTRY_DROPDOWN, country)
        self.fill_input(self.STATE_INPUT, state)
        self.fill_input(self.CITY_INPUT, city)
        self.fill_input(self.ZIPCODE_INPUT, zipcode)
        self.fill_input(self.MOBILE_NUMBER_INPUT, mobile)
        
    def click_create_account(self):
        """Click create account button"""
        self.click_element(self.CREATE_ACCOUNT_BUTTON)
