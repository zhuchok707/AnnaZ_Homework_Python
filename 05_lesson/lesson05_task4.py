from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Открыть Firefox
driver = webdriver.Firefox()

try:
    # Перейти на страницу логина
    driver.get("http://the-internet.herokuapp.com/login")
    time.sleep(1)

    # Ввести username
    username = driver.find_element(By.ID, "username")
    username.send_keys("tomsmith")

    # Ввести password
    password = driver.find_element(By.ID, "password")
    password.send_keys("SuperSecretPassword!")

    # Нажать кнопку Login
    login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_btn.click()
    time.sleep(1)

    # Найти зелёную плашку с сообщением
    success_message = driver.find_element(By.ID, "flash")

    # Вывести текст в консоль без крестика
    print(success_message.text.replace("×", "").strip())

finally:
    # Закрыть браузер
    driver.quit()
