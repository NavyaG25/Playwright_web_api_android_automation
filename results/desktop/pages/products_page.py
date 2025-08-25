"""
Products Page Object Model
"""
from .base_page import BasePage


class ProductsPage(BasePage):
    # Locators
    ALL_PRODUCTS_TEXT = "h2:has-text('All Products')"
    SEARCH_INPUT = "#search_product"
    SEARCH_BUTTON = "#submit_search"
    SEARCHED_PRODUCTS_TEXT = "h2:has-text('Searched Products')"
    PRODUCT_LIST = ".features_items .product-image-wrapper"
    FIRST_PRODUCT_VIEW_BUTTON = ".features_items .product-image-wrapper:first-child a[href*='product_details']"
    
    def __init__(self, page):
        super().__init__(page)
        
    def is_all_products_page_visible(self) -> bool:
        """Verify user is navigated to ALL PRODUCTS page"""
        return self.is_visible(self.ALL_PRODUCTS_TEXT)
        
    def is_products_list_visible(self) -> bool:
        """Verify products list is visible"""
        return self.is_visible(self.PRODUCT_LIST)
        
    def search_product(self, product_name: str):
        """Search for a product"""
        self.fill_input(self.SEARCH_INPUT, product_name)
        self.click_element(self.SEARCH_BUTTON)
        
    def is_searched_products_visible(self) -> bool:
        """Verify 'SEARCHED PRODUCTS' is visible"""
        return self.is_visible(self.SEARCHED_PRODUCTS_TEXT)
        
    def click_view_first_product(self):
        """Click on view product of first product"""
        self.click_element(self.FIRST_PRODUCT_VIEW_BUTTON)
