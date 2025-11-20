from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput")

# вводим текст
driver.find_element(By.ID, "newButtonName").send_keys("SkyPro")

# нажимаем кнопку
driver.find_element(By.ID, "updatingButton").click()

# получаем текст кнопки
btn_text = driver.find_element(By.ID, "updatingButton").text
print(btn_text)

driver.quit()
