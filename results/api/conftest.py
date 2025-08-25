import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
"""
Pytest Configuration for API Testing
"""
import pytest
import requests
import json
import os
from datetime import datetime


@pytest.fixture(scope="session")
def api_base_url():
    """Base URL for API tests"""
    return "https://automationexercise.com/api"


@pytest.fixture(scope="session")
def api_session():
    """Requests session for API tests"""
    session = requests.Session()
    session.headers.update({
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'API-Test-Suite/1.0'
    })
    yield session
    session.close()


@pytest.fixture(autouse=True)
def setup_test_directories():
    """Setup test directories for API tests"""
    directories = [
        "request_response_logs",
        "reports",
        "logs"
    ]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)


@pytest.fixture
def unique_user_data():
    """Generate unique user data for each test"""
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


@pytest.fixture
def test_response_handler():
    """Response handler for saving test data"""
    from utils.api_test_utils import APIResponseHandler
    return APIResponseHandler()


@pytest.fixture
def test_logger():
    """Logger for API tests"""
    from utils.api_test_utils import APITestLogger
    return APITestLogger()



# Utility: Returns API test reporter
def get_reporter():
    """Utility: Returns API test reporter"""
    from .utils.api_test_utils import APITestReporter
    return APITestReporter()


# Hook: Generate beautiful HTML report after all tests
def pytest_sessionfinish(session, exitstatus):
    """Generate beautiful API HTML report after test session finishes."""
    try:
        try:
            # Try relative import now that __init__.py files are present
            from .tests.test_api_automation import reporter
        except ImportError:
            # Fallback: create a new reporter (will not have in-memory results)
            from .utils.api_test_utils import APITestReporter
            reporter = APITestReporter("reports/api_test_execution_summary.json")
        reporter.generate_report()
        from .utils.api_html_report_generator import APIHTMLReportGenerator
        generator = APIHTMLReportGenerator("reports/api_test_execution_summary.json")
        report_path = generator.generate_beautiful_report(output_path="reports/API_Execution_Report.html")
        session.config.pluginmanager.get_plugin("terminalreporter").write_sep(
            "=",
            f"✨ Beautiful API HTML report generated: {report_path}"
        )
    except Exception as e:
        session.config.pluginmanager.get_plugin("terminalreporter").write_sep(
            "=",
            f"❌ Failed to generate beautiful API HTML report: {e}"
        )
