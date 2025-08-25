"""
Test Utilities for Desktop Web Automation
"""
import os
import json
import logging
from datetime import datetime
from typing import Dict, Any



BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
REPORTS_DIR = os.path.join(BASE_DIR, 'reports')
SCREENSHOTS_DIR = os.path.join(BASE_DIR, 'screenshots')

# Singleton paths
STATIC_LOG_FILE = os.path.join(LOGS_DIR, 'execution_log_network_{ts}.txt'.format(ts=datetime.now().strftime('%Y%m%d_%H%M%S')))
STATIC_JSON_FILE = os.path.join(REPORTS_DIR, 'test_execution_summary.json')
STATIC_HTML_FILE = os.path.join(REPORTS_DIR, 'beautiful_desktop_report.html')

class DesktopLogger:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.log_file = STATIC_LOG_FILE
            cls._instance.logger = logging.getLogger("DesktopLoggerSingleton")
            cls._instance.logger.setLevel(logging.INFO)
            cls._instance.logger.propagate = False
            if not cls._instance.logger.handlers:
                os.makedirs(os.path.dirname(cls._instance.log_file), exist_ok=True)
                file_handler = logging.FileHandler(cls._instance.log_file)
                file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
                stream_handler = logging.StreamHandler()
                stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
                cls._instance.logger.addHandler(file_handler)
                cls._instance.logger.addHandler(stream_handler)
        return cls._instance

    def info(self, message: str):
        self.logger.info(message)

    def error(self, message: str):
        self.logger.error(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def info(self, message: str):
        self.logger.info(message)

    def error(self, message: str):
        self.logger.error(message)

    def warning(self, message: str):
        self.logger.warning(message)


class TestDataGenerator:
    @staticmethod
    def generate_unique_user_data() -> Dict[str, str]:
        """Generate unique user data with timestamp"""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return {
            "name": f"TestUser{timestamp}",
            "email": f"testuser{timestamp}@example.com",
            "password": "TestPassword123!",
            "first_name": "Test",
            "last_name": "User",
            "company": "Test Company",
            "address1": "123 Test Street",
            "address2": "Apt 456",
            "country": "United States",
            "state": "California",
            "city": "Los Angeles",
            "zipcode": "90210",
            "mobile": "+1-555-123-4567"
        }



class DesktopReporter:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.report_file = STATIC_JSON_FILE
            cls._instance.test_results = []
        return cls._instance

    def add_test_result(self, test_name: str, status: str, duration: float, details: str = "", screenshots: list = None):
        result = {
            "test_name": test_name,
            "status": status,
            "duration": duration,
            "details": details,
            "screenshots": screenshots or [],
            "timestamp": datetime.now().isoformat()
        }
        self.test_results.append(result)

    def generate_report(self):
        os.makedirs(os.path.dirname(self.report_file), exist_ok=True)
        summary = {
            "total_tests": len(self.test_results),
            "passed": len([r for r in self.test_results if r["status"] == "PASS"]),
            "failed": len([r for r in self.test_results if r["status"] == "FAIL"]),
            "execution_time": datetime.now().isoformat(),
            "test_results": self.test_results
        }
        with open(self.report_file, 'w') as f:
            json.dump(summary, f, indent=2)
        return summary
