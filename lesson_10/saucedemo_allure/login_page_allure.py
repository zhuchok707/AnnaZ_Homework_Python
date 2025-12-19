from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """PageObject страницы логина."""

    URL: str = "https://www.saucedemo.com/"

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def open(self) -> None:
        self.driver.get(self.URL)

    def enter_username(self, username: str) -> None:
        self.driver.find_element(By.ID, "user-name").send_keys(username)

    def enter_password(self, password: str) -> None:
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login(self) -> None:
        self.driver.find_element(By.ID, "login-button").click()
