# SauceDemo Mobile Web Automation Framework

## Overview
This project provides a robust, modern automation framework for testing https://www.saucedemo.com/ on both Android emulators and real Android devices using Playwright (Python) and Pytest. It supports:
- **Mobile emulation** (e.g., Pixel 3)
- **Real Android device automation** via Chrome DevTools Protocol (CDP)
- **Page Object Model (POM)** for maintainable code
- **Detailed logging, screenshots, JSON and beautiful HTML reports**

---

## Project Structure
```
config/         # Settings (device, URL, CDP, headless)
pages/          # Page Object Model classes (login, products, etc.)
utils/          # Helpers: waits, logger, screenshots, reporting, HTML report
conftest.py     # Pytest config/fixtures
tests/          # Test scripts (e.g., test_login.py)
reports/        # JSON and HTML reports
screenshots/    # Screenshots from test runs
logs/           # Log files for each test run
```

---

## Setup Instructions
1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   playwright install
   ```

2. **Configure your environment:**
   - Edit `config/settings.py`:
     - Set `ANDROID_CDP = False` for emulator, `True` for real device.
     - Set `DEVICE = "Pixel 3"` or another supported device for emulation.
     - Set `URL` if you want to test a different site.

---

## Running on Android Emulator (Pixel 3, etc.)
1. Make sure your emulator is running and has internet access.
2. In `config/settings.py`, set:
   ```python
   ANDROID_CDP = False
   DEVICE = "Pixel 3"
   ```
3. Run the test:
   ```sh
   pytest
   ```

---

## Running on Real Android Device (Chrome via CDP)
1. Enable **Developer Options** and **USB Debugging** on your device.
2. Connect your device via USB.
3. Forward the DevTools port:
   ```sh
   adb devices
   adb -s <device_id> forward tcp:9222 localabstract:chrome_devtools_remote
   ```
   Replace `<device_id>` with your device's ID from `adb devices`.
4. Open Chrome on your device (optionally, open https://www.saucedemo.com/).
5. In `config/settings.py`, set:
   ```python
   ANDROID_CDP = True
   ```
6. Run the test:
   ```sh
   pytest
   ```

---

## Output & Reporting
- **Screenshots:** Saved in `screenshots/` (homepage and after login)
- **Logs:** Saved in `logs/` with detailed step-by-step info and device mode
- **Reports:**
  - JSON result in `reports/`
  - Beautiful HTML report auto-generated in `reports/` (open in browser)

## Customization & Extending
- Add new test scenarios in `tests/` and new POM classes in `pages/`
- Adjust device, URL, and CDP settings in `config/settings.py`
- All locators and methods are in `pages/` and `saucedemo_automation_locators.py`

## Troubleshooting
- If both emulator and real device are connected, use `adb -s <device_id> ...` to specify which device to forward.
- If the test fails to find elements, check the logs and screenshots for clues.
- For real device, make sure Chrome is open and port 9222 is forwarded.
- Logs will clearly state which mode (emulator or real device) is being used.

