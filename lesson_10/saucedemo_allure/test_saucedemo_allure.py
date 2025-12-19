import allure
from selenium import webdriver
from login_page_allure import LoginPage
from inventory_page_allure import InventoryPage
from cart_page_allure import CartPage
from checkout_page_allure import CheckoutPage


@allure.title("Тест подсчёта суммы заказа в Saucedemo")
@allure.description(
    "Проверяет, что финальная сумма соответствует ожидаемой "
    "после добавления товаров."
)
@allure.feature("Проверка корзины")
@allure.severity(allure.severity_level.CRITICAL)
def test_saucedemo_total_sum():
    with allure.step("Инициализация WebDriver"):
        driver = webdriver.Firefox()

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    try:
        with allure.step("Открытие страницы входа"):
            login.open()
        with allure.step("Авторизация с валидными данными"):
            login.enter_username("standard_user")
            login.enter_password("secret_sauce")
            login.click_login()

        with allure.step("Добавление товаров в корзину"):
            inventory.add_item_to_cart("Sauce Labs Backpack")
            inventory.add_item_to_cart("Sauce Labs Bolt T-Shirt")
            inventory.add_item_to_cart("Sauce Labs Onesie")
        with allure.step("Переход в корзину"):
            inventory.go_to_cart()

        with allure.step("Переход к оформлению заказа"):
            cart.click_checkout()

        with allure.step("Заполнение формы оформления заказа"):
            checkout.enter_first_name("Ekaterina")
            checkout.enter_last_name("Stennikova")
            checkout.enter_zip("123123")
        with allure.step("Подтверждение оформления заказа"):
            checkout.click_continue()

        with allure.step("Получение итоговой суммы и проверка"):
            total = checkout.get_total()

        assert total.endswith("$58.29")
    finally:
        with allure.step("Закрытие браузера"):
            driver.quit()
