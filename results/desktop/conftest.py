import pytest
import logging
from utils.test_utils import DesktopLogger, DesktopReporter, STATIC_LOG_FILE, STATIC_HTML_FILE
from utils.html_report_generator import HTMLReportGenerator


# Attach shared logger and reporter to pytest config
def pytest_configure(config):
    if not hasattr(config, '_desktop_logger'):
        config._desktop_logger = DesktopLogger()
    if not hasattr(config, '_desktop_reporter'):
        config._desktop_reporter = DesktopReporter()


@pytest.fixture(scope="session")
def desktop_logger(request):
    if not hasattr(request.config, '_desktop_logger'):
        request.config._desktop_logger = DesktopLogger()
    return request.config._desktop_logger

@pytest.fixture(scope="session")
def desktop_reporter(request):
    if not hasattr(request.config, '_desktop_reporter'):
        request.config._desktop_reporter = DesktopReporter()
    return request.config._desktop_reporter

# Generate reports at the end of the session

def pytest_sessionfinish(session, exitstatus):
    # Generate JSON report
    reporter = getattr(session.config, '_desktop_reporter', None)
    html_path = None
    if reporter:
        summary = reporter.generate_report()
        # Only generate HTML if there are results
        if summary and summary.get('total_tests', 0) > 0:
            generator = HTMLReportGenerator()
            html_path = generator.generate_beautiful_report()
    print("\n==============================")
    print(f"Log file: {STATIC_LOG_FILE}")
    if html_path:
        print(f"HTML report generated: {html_path}")
    else:
        print("HTML report was not generated.")
    print("==============================\n")

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Attach reporter to config for sessionfinish
    if not hasattr(config, '_desktop_reporter'):
        config._desktop_reporter = DesktopReporter()
"""
Pytest Configuration for Desktop Web Automation
"""
import pytest
from playwright.sync_api import sync_playwright
import os


@pytest.fixture(scope="session")
def browser_context():
    """Browser context fixture"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            viewport={"width": 1280, "height": 720}
        )
        yield context
        browser.close()


@pytest.fixture
def page(browser_context):
    """Page fixture"""
    page = browser_context.new_page()
    yield page
    page.close()


