"""
API Test Suite for https://automationexercise.com/
This module contains comprehensive API tests for all endpoints
"""



import pytest

import os
import random
import string
from datetime import datetime
from typing import Dict
import requests
import pytest
import json

from ..utils.api_test_utils import APITestLogger, APITestReporter


# Always resolve paths relative to this test file's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGS_DIR = os.path.join(BASE_DIR, "..", "logs")
REPORTS_DIR = os.path.join(BASE_DIR, "..", "reports")
REQRES_DIR = os.path.join(BASE_DIR, "..", "request_response_logs")

# Use a single timestamp for all files per run
SUMMARY_JSON = os.path.join(REPORTS_DIR, "api_test_execution_summary.json")
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
HTML_REPORT = os.path.join(REPORTS_DIR, f"api_test_report_{timestamp}.html")
LOG_FILE = os.path.join(LOGS_DIR, f"api_test_logs_{timestamp}.log")
logger = APITestLogger(log_file=LOG_FILE)
BASE_URL = "https://automationexercise.com/api"

# Use a single global reporter instance for all tests and hooks
reporter = APITestReporter(SUMMARY_JSON)

class APITestClient:
    """API Test Client for automation exercise"""
    def __init__(self):
        self.session = requests.Session()
        self.test_results = []
    def log_request_response(self, method: str, url: str, request_data: Dict, response: requests.Response, test_name=None):
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "method": method,
            "url": url,
            "request_data": request_data,
            "response_status": response.status_code,
            "response_headers": dict(response.headers),
            "response_body": response.text
        }
        reqres_dir = os.path.join(BASE_DIR, "..", "request_response_logs")
        reqres_filename = f"{test_name or 'api_test'}_{method}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        reqres_path = os.path.join(reqres_dir, reqres_filename)
        with open(reqres_path, 'w', encoding='utf-8') as f:
            json.dump(log_entry, f, indent=2)
        logger.info(f"{method} {url} - Status: {response.status_code}")
    def generate_random_email(self):
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return f"test_{random_string}@example.com"
    def generate_test_user_data(self):
        random_id = ''.join(random.choices(string.digits, k=6))
        return {
            "name": f"Test User {random_id}",
            "email": self.generate_random_email(),
            "password": "testpassword123",
            "title": "Mr",
            "birth_date": "15",
            "birth_month": "January",
            "birth_year": "1990",
            "firstname": f"Test{random_id}",
            "lastname": "User",
            "company": "Test Company",
            "address1": "123 Test Street",
            "address2": "Apt 456",
            "country": "United States",
            "zipcode": "12345",
            "state": "California",
            "city": "Los Angeles",
            "mobile_number": "1234567890"
        }

@pytest.fixture
def api_client():
    return APITestClient()

@pytest.fixture
def test_user_data(api_client):
    return api_client.generate_test_user_data()

class TestAutomationExerciseAPI:
    def test_01_get_user_detail_by_email_invalid(self, api_client, request):
        url = f"{BASE_URL}/getUserDetailByEmail"
        params = {"email": "nonexistent@example.com"}
        response = api_client.session.get(url, params=params)
        api_client.log_request_response("GET", url, params, response, test_name="test_01_get_user_detail_by_email_invalid")
        status = "PASS" if response.status_code in [200, 404] else "FAIL"
        # Add to reporter
        reporter.add_test_result(
            test_name="GET user detail by email - Invalid email",
            api_endpoint=url,
            method="GET",
            status_code=response.status_code,
            response_time=response.elapsed.total_seconds() * 1000 if hasattr(response, 'elapsed') else 0,
            status="PASS" if response.status_code in [200, 404] else "FAIL",
            details=f"Response: {response.text[:100]}..."
        )
        assert response.status_code in [200, 404], f"Expected 200 or 404, got {response.status_code}"
        logger.info("✓ Test 1 Passed: GET user detail by email (invalid)")

    def test_02_create_user_account(self, api_client, test_user_data, request):
        url = f"{BASE_URL}/createAccount"
        response = api_client.session.post(url, data=test_user_data)
        api_client.log_request_response("POST", url, test_user_data, response, test_name="test_02_create_user_account")
        status = "PASS" if response.status_code in [200, 201] else "FAIL"
        # Add to reporter
        reporter.add_test_result(
            test_name="POST To Create/Register User Account",
            api_endpoint=url,
            method="POST",
            status_code=response.status_code,
            response_time=response.elapsed.total_seconds() * 1000 if hasattr(response, 'elapsed') else 0,
            status="PASS" if response.status_code in [200, 201] else "FAIL",
            details=f"Response: {response.text[:100]}..."
        )
        assert response.status_code in [200, 201], f"Expected 200/201, got {response.status_code}"
        api_client.created_user = test_user_data
        if "User created!" in response.text or "created" in response.text.lower():
            logger.info("✓ Test 2 Passed: User account created successfully")
        else:
            logger.warning(f"Test 2: Unexpected response content: {response.text}")

    def test_03_verify_login_valid(self, api_client, test_user_data, request):
        url = f"{BASE_URL}/verifyLogin"
        login_data = {"email": test_user_data["email"], "password": test_user_data["password"]}
        response = api_client.session.post(url, data=login_data)
        api_client.log_request_response("POST", url, login_data, response, test_name="test_03_verify_login_valid")
        status = "PASS" if response.status_code == 200 else "FAIL"
        # Add to reporter
        reporter.add_test_result(
            test_name="POST To Verify Login with valid details",
            api_endpoint=url,
            method="POST",
            status_code=response.status_code,
            response_time=response.elapsed.total_seconds() * 1000 if hasattr(response, 'elapsed') else 0,
            status="PASS" if response.status_code == 200 else "FAIL",
            details=f"Response: {response.text[:100]}..."
        )
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        response_text = response.text.lower()
        if "user exists" in response_text or "success" in response_text:
            logger.info("✓ Test 3 Passed: Login verification successful")
        else:
            logger.info(f"Test 3: Response content: {response.text}")

    def test_04_verify_login_invalid(self, api_client, request):
        url = f"{BASE_URL}/verifyLogin"
        login_data = {"email": "invalid@example.com", "password": "wrongpassword"}
        response = api_client.session.post(url, data=login_data)
        api_client.log_request_response("POST", url, login_data, response, test_name="test_04_verify_login_invalid")
        status = "PASS" if response.status_code in [200, 401, 404] else "FAIL"
        # Add to reporter
        reporter.add_test_result(
            test_name="POST To Verify Login with invalid details",
            api_endpoint=url,
            method="POST",
            status_code=response.status_code,
            response_time=response.elapsed.total_seconds() * 1000 if hasattr(response, 'elapsed') else 0,
            status="PASS" if response.status_code in [200, 401, 404] else "FAIL",
            details=f"Response: {response.text[:100]}..."
        )
        assert response.status_code in [200, 401, 404], f"Expected 200/401/404, got {response.status_code}"
        logger.info("✓ Test 4 Passed: Invalid login handled correctly")

    def test_05_search_product(self, api_client, request):
        url = f"{BASE_URL}/searchProduct"
        search_terms = ["top", "tshirt", "jean", "dress"]
        for idx, term in enumerate(search_terms, 1):
            search_data = {"search_product": term}
            response = api_client.session.post(url, data=search_data)
            api_client.log_request_response("POST", url, search_data, response, test_name=f"test_05_search_product_{idx}")
            status = "PASS" if response.status_code == 200 else "FAIL"
            # Add to reporter
            reporter.add_test_result(
                test_name=f"POST To Search Product - '{term}'",
                api_endpoint=url,
                method="POST",
                status_code=response.status_code,
                response_time=response.elapsed.total_seconds() * 1000 if hasattr(response, 'elapsed') else 0,
                status="PASS" if response.status_code == 200 else "FAIL",
                details=f"Response: {response.text[:100]}..."
            )
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            try:
                products = response.json()
                logger.info(f"✓ Search for '{term}' returned {len(products.get('products', []))} products")
            except json.JSONDecodeError:
                logger.info(f"✓ Search for '{term}' completed - Response: {response.text[:100]}...")

    def test_06_get_all_products_list(self, api_client, request):
        url = f"{BASE_URL}/productsList"
        response = api_client.session.get(url)
        api_client.log_request_response("GET", url, {}, response, test_name="test_06_get_all_products_list")
        status = "PASS" if response.status_code == 200 else "FAIL"
        # Add to reporter
        reporter.add_test_result(
            test_name="GET All Products List",
            api_endpoint=url,
            method="GET",
            status_code=response.status_code,
            response_time=response.elapsed.total_seconds() * 1000 if hasattr(response, 'elapsed') else 0,
            status="PASS" if response.status_code == 200 else "FAIL",
            details=f"Response: {response.text[:100]}..."
        )
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        try:
            products = response.json()
            logger.info(f"✓ Retrieved products list with {len(products.get('products', []))} products")
        except json.JSONDecodeError:
            logger.info("✓ Products list retrieved successfully")

    def test_07_get_all_brands_list(self, api_client, request):
        url = f"{BASE_URL}/brandsList"
        response = api_client.session.get(url)
        api_client.log_request_response("GET", url, {}, response, test_name="test_07_get_all_brands_list")
        status = "PASS" if response.status_code == 200 else "FAIL"
        # Add to reporter
        reporter.add_test_result(
            test_name="GET All Brands List",
            api_endpoint=url,
            method="GET",
            status_code=response.status_code,
            response_time=response.elapsed.total_seconds() * 1000 if hasattr(response, 'elapsed') else 0,
            status="PASS" if response.status_code == 200 else "FAIL",
            details=f"Response: {response.text[:100]}..."
        )
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        try:
            brands = response.json()
            logger.info(f"✓ Retrieved brands list with {len(brands.get('brands', []))} brands")
        except json.JSONDecodeError:
            logger.info("✓ Brands list retrieved successfully")

    def test_08_delete_user_account(self, api_client, test_user_data, request):
        url = f"{BASE_URL}/deleteAccount"
        delete_data = {"email": test_user_data["email"], "password": test_user_data["password"]}
        response = api_client.session.delete(url, data=delete_data)
        api_client.log_request_response("DELETE", url, delete_data, response, test_name="test_08_delete_user_account")
        status = "PASS" if response.status_code in [200, 404] else "FAIL"
        # Add to reporter
        reporter.add_test_result(
            test_name="DELETE METHOD To Delete User Account",
            api_endpoint=url,
            method="DELETE",
            status_code=response.status_code,
            response_time=response.elapsed.total_seconds() * 1000 if hasattr(response, 'elapsed') else 0,
            status="PASS" if response.status_code in [200, 404] else "FAIL",
            details=f"Response: {response.text[:100]}..."
        )
        assert response.status_code in [200, 404], f"Expected 200 or 404, got {response.status_code}"
        if "Account deleted!" in response.text or "deleted" in response.text.lower():
            logger.info("✓ Test 8 Passed: User account deleted successfully")
        else:
            logger.info(f"Test 8: Response content: {response.text}")


def pytest_sessionfinish(session, exitstatus):
    reporter.generate_report()
    # Save the HTML report using the new summary file
    try:
        from utils.api_html_report_generator import APIHTMLReportGenerator
        generator = APIHTMLReportGenerator(SUMMARY_JSON)
        report_path = generator.generate_beautiful_report(output_path=HTML_REPORT)
        session.config.pluginmanager.get_plugin("terminalreporter").write_sep(
            "=",
            f"✨ Beautiful API HTML report generated: {report_path}"
        )
    except Exception as e:
        session.config.pluginmanager.get_plugin("terminalreporter").write_sep(
            "=",
            f"❌ Failed to generate beautiful API HTML report: {e}"
        )
