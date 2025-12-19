from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """PageObject корзины."""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def click_checkout(self) -> None:
        self.driver.find_element(By.ID, "checkout").click()
