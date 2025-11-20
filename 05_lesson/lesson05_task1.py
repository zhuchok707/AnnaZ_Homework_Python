from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/classattr")
    time.sleep(1)

    xpath = (
        "//button[contains(concat(' ', normalize-space(@class), ' '), "
        "' btn-primary ')]"
    )
    button = driver.find_element(By.XPATH, xpath)

    button.click()
    time.sleep(0.5)

    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(1)

finally:
    driver.quit()
