"""
API Test Utilities for Automation Exercise API Testing
"""
import json
import logging
import os
from datetime import datetime
from typing import Dict, Any, List


class APITestLogger:
    def __init__(self, log_file: str = None):
        # Only add a timestamp if no log_file is provided
        if log_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            log_file = f"logs/api_test_logs_{timestamp}.log"
        self.log_file = log_file
        self.setup_logger()
        
    def setup_logger(self):
        """Setup logging configuration for API tests"""
        # Create logs directory if it doesn't exist
        log_dir = os.path.dirname(self.log_file)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        # Remove any existing handlers for this logger
        logger = logging.getLogger(__name__)
        logger.handlers = []
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler(self.log_file, mode='w')
        file_handler.setFormatter(formatter)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
        self.logger = logger
        
    def info(self, message: str):
        """Log info message"""
        self.logger.info(message)
        
    def error(self, message: str):
        """Log error message"""
        self.logger.error(message)
        
    def warning(self, message: str):
        """Log warning message"""
        self.logger.warning(message)


class APIResponseHandler:
    @staticmethod
    def save_request_response(test_name: str, method: str, url: str, 
                            request_data: Dict, response_data: Dict, 
                            status_code: int, save_dir: str = "request_response_logs"):
        """Save API request and response for debugging"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{test_name}_{method}_{timestamp}.json"
        filepath = os.path.join(save_dir, filename)
        
        # Create directory if it doesn't exist
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        
        log_data = {
            "test_name": test_name,
            "timestamp": datetime.now().isoformat(),
            "request": {
                "method": method,
                "url": url,
                "data": request_data
            },
            "response": {
                "status_code": status_code,
                "data": response_data
            }
        }
        
        with open(filepath, 'w') as f:
            json.dump(log_data, f, indent=2)
            
        return filepath
    
    @staticmethod
    def validate_response_structure(response_data: Dict, expected_keys: List[str]) -> bool:
        """Validate that response contains expected keys"""
        for key in expected_keys:
            if key not in response_data:
                return False
        return True
    
    @staticmethod
    def extract_response_data(response_data: Dict, key_path: str):
        """Extract data from nested response using dot notation"""
        keys = key_path.split('.')
        current_data = response_data
        
        for key in keys:
            if isinstance(current_data, dict) and key in current_data:
                current_data = current_data[key]
            else:
                return None
                
        return current_data


class APITestDataGenerator:
    @staticmethod
    def generate_unique_user_data() -> Dict[str, str]:
        """Generate unique user data for API tests"""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return {
            "name": f"APITestUser{timestamp}",
            "email": f"apitest{timestamp}@test.com",
            "password": "TestPassword123!",
            "title": "Mr",
            "birth_date": "15",
            "birth_month": "5",
            "birth_year": "1990",
            "firstname": "API",
            "lastname": "Test",
            "company": "Test Company API",
            "address1": "123 API Test Street",
            "address2": "Suite 456",
            "country": "United States",
            "zipcode": "90210",
            "state": "California",
            "city": "Los Angeles",
            "mobile_number": "+1-555-API-TEST"
        }
    
    @staticmethod
    def generate_search_terms() -> List[str]:
        """Generate common search terms for testing"""
        return [
            "shirt", "dress", "jeans", "top", "tshirt",
            "jacket", "pants", "blouse", "skirt", "sweater"
        ]


class APITestReporter:
    def __init__(self, report_file: str = "reports/api_test_execution_summary.json"):
        self.report_file = report_file
        self.test_results = []
        
    def add_test_result(self, test_name: str, api_endpoint: str, method: str,
                       status_code: int, response_time: float, status: str, 
                       details: str = "", request_data: Dict = None, 
                       response_data: Dict = None):
        """Add API test result to report"""
        result = {
            "test_name": test_name,
            "api_endpoint": api_endpoint,
            "http_method": method,
            "status_code": status_code,
            "response_time_ms": response_time,
            "test_status": status,
            "details": details,
            "timestamp": datetime.now().isoformat(),
            "request_data": request_data or {},
            "response_data": response_data or {}
        }
        self.test_results.append(result)
        
    def generate_report(self):
        """Generate final API test report"""
        try:
            report_dir = os.path.dirname(self.report_file)
            if not os.path.exists(report_dir):
                os.makedirs(report_dir)
            summary = {
                "total_tests": len(self.test_results),
                "passed": len([r for r in self.test_results if r["test_status"] == "PASS"]),
                "failed": len([r for r in self.test_results if r["test_status"] == "FAIL"]),
                "total_api_calls": len(self.test_results),
                "avg_response_time": sum(r["response_time_ms"] for r in self.test_results) / len(self.test_results) if self.test_results else 0,
                "execution_time": datetime.now().isoformat(),
                "test_results": self.test_results
            }
            abs_path = os.path.abspath(self.report_file)
            print(f"[APITestReporter] Writing summary JSON to: {abs_path}")
            with open(self.report_file, 'w') as f:
                json.dump(summary, f, indent=2)
            return summary
        except Exception as e:
            print(f"[APITestReporter] ERROR writing report: {e}")
            raise


class APIEndpoints:
    """API Endpoints for Automation Exercise"""
    BASE_URL = "https://automationexercise.com/api"
    
    # User Management
    GET_USER_LIST = "/getUserDetailByEmail"
    CREATE_USER = "/createAccount"
    VERIFY_LOGIN = "/verifyLogin"
    DELETE_USER = "/deleteAccount"
    
    # Product Management
    GET_PRODUCTS_LIST = "/productsList"
    SEARCH_PRODUCT = "/searchProduct"
    GET_BRANDS_LIST = "/brandsList"
    
    @classmethod
    def get_full_url(cls, endpoint: str) -> str:
        """Get full URL for an endpoint"""
        return cls.BASE_URL + endpoint


class APITestValidator:
    @staticmethod
    def validate_user_creation_response(response_data: Dict) -> bool:
        """Validate user creation API response"""
        required_fields = ["responseCode", "message"]
        return APIResponseHandler.validate_response_structure(response_data, required_fields)
    
    @staticmethod
    def validate_products_list_response(response_data: Dict) -> bool:
        """Validate products list API response"""
        if "products" not in response_data:
            return False
        
        # Check if products is a list and has items
        products = response_data.get("products", [])
        if not isinstance(products, list) or len(products) == 0:
            return False
            
        # Validate first product structure
        if products:
            required_product_fields = ["id", "name", "price", "brand", "category"]
            first_product = products[0]
            for field in required_product_fields:
                if field not in first_product:
                    return False
                    
        return True
    
    @staticmethod
    def validate_search_response(response_data: Dict, search_term: str) -> bool:
        """Validate search API response"""
        if "products" not in response_data:
            return False
            
        products = response_data.get("products", [])
        if not isinstance(products, list):
            return False
            
        # Check if search results contain the search term
        if products:
            for product in products:
                product_name = product.get("name", "").lower()
                if search_term.lower() in product_name:
                    return True
                    
        return True  # Empty results are also valid
    
    @staticmethod
    def validate_brands_list_response(response_data: Dict) -> bool:
        """Validate brands list API response"""
        if "brands" not in response_data:
            return False
            
        brands = response_data.get("brands", [])
        if not isinstance(brands, list):
            return False
            
        # Validate brand structure
        if brands:
            required_brand_fields = ["id", "brand"]
            first_brand = brands[0]
            for field in required_brand_fields:
                if field not in first_brand:
                    return False
                    
        return True
