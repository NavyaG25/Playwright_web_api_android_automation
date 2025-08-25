"""
Desktop Web Automation Tests for https://automationexercise.com/
Test Case 1: Register User
Test Case 4: Search Product
"""
import pytest
import time
from pages.home_page import HomePage
from pages.signup_login_page import SignupLoginPage
from pages.account_information_page import AccountInformationPage
from pages.account_created_page import AccountCreatedPage
from pages.products_page import ProductsPage
from utils.test_utils import DesktopLogger, TestDataGenerator, DesktopReporter



class TestDesktopWebAutomation:
    def test_register_user(self, page, desktop_logger, desktop_reporter):
        """Test Case 1: Register User"""
        start_time = time.time()
        test_name = "Test Case 1: Register User"
        screenshots = []
        
        from utils.test_utils import TestDataGenerator
        test_data = TestDataGenerator()
        try:
            desktop_logger.info(f"Starting {test_name}")
            
            # Initialize page objects
            home_page = HomePage(page)
            signup_page = SignupLoginPage(page)
            account_info_page = AccountInformationPage(page)
            account_created_page = AccountCreatedPage(page)
            
            # Generate unique user data
            user_data = test_data.generate_unique_user_data()
            
            # Step 1-2: Launch browser and navigate to homepage
            desktop_logger.info("Navigating to homepage")
            home_page.navigate_to_home()
            
            # Step 3: Verify home page is visible
            assert home_page.is_home_page_visible(), "Home page is not visible"
            desktop_logger.info("Home page verified successfully")
            screenshot = home_page.take_screenshot("01_homepage_loaded")
            screenshots.append(screenshot)
            
            # Step 4: Click on 'Signup / Login' button
            desktop_logger.info("Clicking Signup/Login button")
            home_page.click_signup_login()
            
            # Step 5: Verify 'New User Signup!' is visible
            assert signup_page.is_new_user_signup_visible(), "New User Signup text not visible"
            desktop_logger.info("New User Signup section verified")
            screenshot = signup_page.take_screenshot("02_signup_login_page")
            screenshots.append(screenshot)
            
            # Step 6: Enter name and email address
            desktop_logger.info(f"Filling signup details for user: {user_data['name']}")
            signup_page.fill_signup_details(user_data['name'], user_data['email'])
            
            # Step 7: Click 'Signup' button
            desktop_logger.info("Clicking Signup button")
            signup_page.click_signup_button()
            
            # Step 8: Verify 'ENTER ACCOUNT INFORMATION' is visible
            assert account_info_page.is_enter_account_info_visible(), "Enter Account Information text not visible"
            desktop_logger.info("Enter Account Information page verified")
            screenshot = account_info_page.take_screenshot("03_account_information_page")
            screenshots.append(screenshot)
            
            # Step 9: Fill account information
            desktop_logger.info("Filling account information")
            account_info_page.select_title("Mr")
            account_info_page.fill_account_information(
                user_data['password'], "15", "5", "1990"
            )
            
            # Step 10-11: Select checkboxes
            account_info_page.select_newsletter()
            account_info_page.select_special_offers()
            
            # Step 12: Fill address details
            desktop_logger.info("Filling address information")
            account_info_page.fill_address_information(
                user_data['first_name'], user_data['last_name'], user_data['company'],
                user_data['address1'], user_data['address2'], user_data['country'],
                user_data['state'], user_data['city'], user_data['zipcode'], user_data['mobile']
            )
            
            # Step 13: Click 'Create Account' button
            desktop_logger.info("Clicking Create Account button")
            account_info_page.click_create_account()
            
            # Step 14: Verify 'ACCOUNT CREATED!' is visible
            assert account_created_page.is_account_created_visible(), "Account Created text not visible"
            desktop_logger.info("Account created successfully")
            screenshot = account_created_page.take_screenshot("04_account_created_success")
            screenshots.append(screenshot)
            
            # Continue to home page
            account_created_page.click_continue()
            screenshot = home_page.take_screenshot("05_logged_in_homepage")
            screenshots.append(screenshot)
            
            # Verify user is logged in
            assert home_page.is_user_logged_in(), "User is not logged in"
            desktop_logger.info(f"User successfully logged in: {user_data['name']}")
            
            end_time = time.time()
            duration = end_time - start_time
            
            desktop_reporter.add_test_result(
                test_name, "PASS", duration, 
                f"User registration completed successfully for {user_data['name']}", 
                screenshots
            )
            desktop_logger.info(f"{test_name} completed successfully in {duration:.2f} seconds")
            
        except Exception as e:
            end_time = time.time()
            duration = end_time - start_time
            error_msg = f"Test failed with error: {str(e)}"
            desktop_logger.error(error_msg)
            desktop_reporter.add_test_result(test_name, "FAIL", duration, error_msg, screenshots)
            raise
    
    def test_search_product(self, page, desktop_logger, desktop_reporter):
        """Test Case 4: Search Product"""
        start_time = time.time()
        test_name = "Test Case 4: Search Product"
        screenshots = []
        
        from utils.test_utils import TestDataGenerator
        test_data = TestDataGenerator()
        try:
            desktop_logger.info(f"Starting {test_name}")
            
            # Initialize page objects
            home_page = HomePage(page)
            products_page = ProductsPage(page)
            
            # Step 1-2: Launch browser and navigate to homepage
            desktop_logger.info("Navigating to homepage")
            home_page.navigate_to_home()
            
            # Step 3: Verify home page is visible
            assert home_page.is_home_page_visible(), "Home page is not visible"
            desktop_logger.info("Home page verified successfully")
            screenshot = home_page.take_screenshot("06_homepage_for_search")
            screenshots.append(screenshot)
            
            # Step 4: Click on 'Products' button
            desktop_logger.info("Clicking Products button")
            home_page.click_products()
            
            # Step 5: Verify user is navigated to ALL PRODUCTS page
            assert products_page.is_all_products_page_visible(), "All Products page not visible"
            desktop_logger.info("All Products page verified")
            
            # Step 6: Verify products list is visible
            assert products_page.is_products_list_visible(), "Products list not visible"
            desktop_logger.info("Products list verified")
            screenshot = products_page.take_screenshot("07_products_page")
            screenshots.append(screenshot)
            
            # Step 7: Search for product
            search_term = "dress"
            desktop_logger.info(f"Searching for product: {search_term}")
            products_page.search_product(search_term)
            
            # Step 8: Verify 'SEARCHED PRODUCTS' is visible
            assert products_page.is_searched_products_visible(), "Searched Products text not visible"
            desktop_logger.info("Search results verified")
            screenshot = products_page.take_screenshot("08_search_results")
            screenshots.append(screenshot)
            
            # Step 9: Verify search results are related to the search term
            # Note: This would require additional verification logic for product content
            desktop_logger.info(f"Search for '{search_term}' completed successfully")
            
            end_time = time.time()
            duration = end_time - start_time
            
            desktop_reporter.add_test_result(
                test_name, "PASS", duration, 
                f"Product search completed successfully for '{search_term}'", 
                screenshots
            )
            desktop_logger.info(f"{test_name} completed successfully in {duration:.2f} seconds")
            
        except Exception as e:
            end_time = time.time()
            duration = end_time - start_time
            error_msg = f"Test failed with error: {str(e)}"
            desktop_logger.error(error_msg)
            desktop_reporter.add_test_result(test_name, "FAIL", duration, error_msg, screenshots)
            raise
