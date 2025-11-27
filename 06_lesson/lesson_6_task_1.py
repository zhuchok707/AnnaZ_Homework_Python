from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/ajax")

# нажимаем синюю кнопку
driver.find_element(By.ID, "ajaxButton").click()

# ждём появления зелёной плашки и текста
element = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
)

print(element.text)  # Должно быть: "Data loaded with AJAX get request."

driver.quit()
