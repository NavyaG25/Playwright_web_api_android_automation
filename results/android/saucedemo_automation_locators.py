# Locators and interaction methods for SauceDemo (for reuse)

LOGIN_USERNAME = "#user-name"
LOGIN_PASSWORD = "#password"
LOGIN_BUTTON = "#login-button"
PRODUCTS_TEXT = "text=Products"

async def login(page, username: str, password: str):
    await page.fill(LOGIN_USERNAME, username)
    await page.fill(LOGIN_PASSWORD, password)
    await page.click(LOGIN_BUTTON)
