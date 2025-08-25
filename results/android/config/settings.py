# Configuration for Playwright mobile web automation

URL = "https://www.saucedemo.com/"
DEVICE = "Pixel 3"
HEADLESS = False  # Set True for headless mode
ANDROID_CDP = True  # Set True to use real Android device with Chrome via CDP

# Chrome DevTools Protocol (CDP) settings for real device
CDP_HOST = "localhost"
CDP_PORT = 9222  # Default port for remote debugging
