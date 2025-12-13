from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


def test_saucedemo_total_sum():
    driver = webdriver.Firefox()

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.open()
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    inventory.add_item_to_cart("Sauce Labs Backpack")
    inventory.add_item_to_cart("Sauce Labs Bolt T-Shirt")
    inventory.add_item_to_cart("Sauce Labs Onesie")
    inventory.go_to_cart()

    cart.click_checkout()

    checkout.enter_first_name("Anna")
    checkout.enter_last_name("Zhukova")
    checkout.enter_zip("123456")
    checkout.click_continue()

    total = checkout.get_total()

    driver.quit()

    assert total.endswith("$58.29")
