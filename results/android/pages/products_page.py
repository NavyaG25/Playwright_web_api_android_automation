from playwright.async_api import Page

class ProductsPage:
    PRODUCTS_TEXT = "text=Products"

    def __init__(self, page: Page):
        self.page = page

    async def is_loaded(self) -> bool:
        return await self.page.is_visible(self.PRODUCTS_TEXT)
