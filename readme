# Playwright API, Desktop Web & Mobile web Automation Framework

Unified automation framework for desktop web, mobile web, and API testing using Playwright, Pytest, and modern reporting.

## Overview

This repository provides a modular, scalable automation solution for:
- Mobile web testing (Android emulator & real device via Chrome DevTools)
- Desktop web automation
- API testing and validation

It implements the Page Object Model (POM), detailed logging, screenshot capture, and generates both JSON and HTML reports for all test runs. The framework is designed for maintainability, extensibility, and professional reporting.

## Features

- Mobile web automation on Android emulators and real devices
- Desktop web automation with Playwright
- API test automation with requests and Pytest
- Page Object Model for maintainable test code
- Rich HTML and JSON reporting for all test types
- Automatic screenshot capture after every test run
- Detailed logging for every test run
- Environment and device configuration via settings
- Modular utilities for waits, logging, reporting, and screenshots

## Tech Stack

- Python 3.11+
- Playwright
- Pytest
- Pytest-HTML
- Allure-Pytest (API)
- Requests (API)
- JSONSchema, Pydantic (API validation)
- ADB (for real device mobile automation)
- Chrome DevTools Protocol (CDP) for mobile

## Project Structure

```
results/
  android/
    config/           # Device, URL, CDP, headless settings
    pages/            # Mobile POM classes (login, products, etc.)
    utils/            # Waits, logger, screenshots, reporting
    tests/            # Mobile test scripts (e.g., test_login.py)
    reports/          # JSON and HTML reports
    screenshots/      # Screenshots from test runs
    logs/             # Log files for each test run
    conftest.py       # Pytest config/fixtures
    requirements.txt
  desktop/
    pages/            # Desktop POM classes
    utils/            # Desktop utilities
    tests/            # Desktop test scripts
    reports/          # Desktop test reports
    screenshots/      # Desktop screenshots
    logs/             # Desktop logs
    conftest.py
    requirements.txt
  api/
    tests/            # API test scripts
    reports/          # API test reports
    logs/             # API logs
    request_response_logs/ # Raw API request/response logs
    conftest.py
    requirements.txt
```

## Installation and Prerequisites

1. **Clone the repository** and navigate to the desired environment (`android`, `desktop`, or `api`).
2. **Install dependencies** for the chosen environment:
   ```sh
   pip install -r requirements.txt
   playwright install
   ```
3. **For mobile automation:**
   - Install ADB and set up Android emulator or connect a real device.
   - Configure `config/settings.py` for device, URL, and CDP options.

## Usage

### Mobile Web (Android)

- **Emulator:**
  - Start emulator, set `ANDROID_CDP = False` in `config/settings.py`.
  - Run tests:
    ```sh
    pytest
    ```
- **Real Device:**
  - Enable USB debugging, connect device, forward port with ADB.
  - Set `ANDROID_CDP = True` in `config/settings.py`.
  - Run tests:
    ```sh
    pytest
    ```

### Desktop Web

- Navigate to `desktop/`, install dependencies, and run:
  ```sh
  pytest
  ```

### API Testing

- Navigate to `api/`, install dependencies, and run:
  ```sh
  pytest
  ```

### Output

- **Reports:** HTML and JSON reports in `reports/`
- **Screenshots:** Saved in `screenshots/`
- **Logs:** Saved in `logs/`

## CI/CD Integration

- Pytest is configured for HTML and JSON reporting for all environments.
- Reports and logs are generated automatically for each test run.
- Artifacts (reports, logs, screenshots) are organized per environment for easy integration with CI/CD pipelines.
- Markers and configuration in `pytest.ini` files support test selection and reporting in automated pipelines.
