from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class InventoryPage:
    """PageObject страницы товаров."""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def add_item_to_cart(self, item_name: str) -> None:
        self.driver.find_element(
            By.XPATH,
            f"//div[text()='{item_name}']/../../..//button"
        ).click()

    def go_to_cart(self) -> None:
        self.driver.find_element(
            By.CLASS_NAME,
            "shopping_cart_link"
        ).click()
