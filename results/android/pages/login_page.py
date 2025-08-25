from playwright.async_api import Page
from typing import Any

class LoginPage:
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    PRODUCTS_TEXT = "text=Products"

    def __init__(self, page: Page):
        self.page = page

    async def enter_username(self, username: str):
        await self.page.fill(self.USERNAME_INPUT, username)

    async def enter_password(self, password: str):
        await self.page.fill(self.PASSWORD_INPUT, password)

    async def click_login(self):
        await self.page.click(self.LOGIN_BUTTON)

    async def is_products_visible(self) -> bool:
        return await self.page.is_visible(self.PRODUCTS_TEXT)
