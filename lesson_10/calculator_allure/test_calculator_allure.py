import allure
from selenium import webdriver
from calculator_page_allure import CalculatorPage


@allure.title("Проверка работы калькулятора")
@allure.description("Проверка сложения 7 + 8")
@allure.feature("Calculator")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_result():
    driver = webdriver.Chrome()
    page = CalculatorPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        page.open()

    with allure.step("Установить задержку"):
        page.set_delay("45")

    with allure.step("Ввести выражение 7 + 8"):
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")

    with allure.step("Проверить результат"):
        page.wait_for_result("15")
        assert page.get_result() == "15"

    driver.quit()
