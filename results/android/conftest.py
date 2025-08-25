import pytest
from config import settings
from utils.logger import log_info

@pytest.fixture(scope="session", autouse=True)
def print_test_env():
    log_info(f"Test running on: {settings.URL} | Device: {settings.DEVICE} | Headless: {settings.HEADLESS}")
