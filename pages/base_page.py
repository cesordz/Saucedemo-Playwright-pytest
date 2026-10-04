from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navegar(self, ruta: str = ""):
        self.page.goto(f"/{ruta.lstrip('/')}")

    def obtener_url_actual(self) -> str:
        return self.page.url
