import json
from pathlib import Path
import pytest
import allure
from playwright.sync_api import Page

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def cargar_datos(nombre_archivo: str) -> dict:
    ruta = DATA_DIR / nombre_archivo
    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


@pytest.fixture(scope="session")
def datos_usuarios() -> dict:
    return cargar_datos("users.json")


@pytest.fixture(scope="session")
def datos_checkout() -> dict:
    return cargar_datos("checkout_data.json")


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "base_url": "https://www.saucedemo.com",
        "viewport": {"width": 1280, "height": 720},
    }


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        page: Page = item.funcargs.get("page")
        if page:
            allure.attach(
                page.screenshot(full_page=True),
                name="screenshot_fallo",
                attachment_type=allure.attachment_type.PNG,
            )
