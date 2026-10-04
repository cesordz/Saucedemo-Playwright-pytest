from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    USUARIO_INPUT = '[data-test="username"]'
    PASSWORD_INPUT = '[data-test="password"]'
    LOGIN_BUTTON = '[data-test="login-button"]'
    ERROR_MENSAJE = '[data-test="error"]'

    def __init__(self, page: Page):
        super().__init__(page)

    def abrir(self):
        self.navegar("")

    def ingresar_usuario(self, usuario: str):
        self.page.locator(self.USUARIO_INPUT).fill(usuario)

    def ingresar_password(self, password: str):
        self.page.locator(self.PASSWORD_INPUT).fill(password)

    def hacer_clic_en_login(self):
        self.page.locator(self.LOGIN_BUTTON).click()

    def iniciar_sesion(self, usuario: str, password: str):
        self.ingresar_usuario(usuario)
        self.ingresar_password(password)
        self.hacer_clic_en_login()

    def obtener_mensaje_error(self) -> str:
        return self.page.locator(self.ERROR_MENSAJE).inner_text()

    def es_mensaje_error_visible(self) -> bool:
        return self.page.locator(self.ERROR_MENSAJE).is_visible()
