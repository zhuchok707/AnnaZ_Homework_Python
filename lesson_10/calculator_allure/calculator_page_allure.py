from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    """PageObject страницы медленного калькулятора."""

    URL: str = (
        "https://bonigarcia.dev/"
        "selenium-webdriver-java/slow-calculator.html"
    )

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы калькулятора.

        :param driver: экземпляр WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open(self) -> None:
        """Открывает страницу калькулятора."""
        self.driver.get(self.URL)

    def set_delay(self, value: str) -> None:
        """
        Устанавливает задержку вычислений.

        :param value: значение задержки
        """
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(value)

    def click_button(self, value: str) -> None:
        """
        Нажимает кнопку калькулятора.

        :param value: текст кнопки
        """
        button = self.driver.find_element(
            By.XPATH,
            f"//span[text()='{value}']"
        )
        button.click()

    def wait_for_result(self, expected: str) -> bool:
        """
        Ожидает появления ожидаемого результата.

        :param expected: ожидаемый результат
        :return: True, если результат появился
        """
        return self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"),
                expected
            )
        )

    def get_result(self) -> str:
        """
        Возвращает результат вычисления.

        :return: текст результата
        """
        return self.driver.find_element(
            By.CSS_SELECTOR,
            ".screen"
        ).text
