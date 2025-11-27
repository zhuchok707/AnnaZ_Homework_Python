from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

url = (
    "https://bonigarcia.dev/selenium-webdriver-java/"
    "loading-images.html"
)
driver.get(url)

wait = WebDriverWait(driver, 10)


img3 = wait.until(
    EC.presence_of_element_located((By.ID, "award"))
)


wait.until(
    lambda d: img3.get_attribute("src") not in (None, "")
)

src = img3.get_attribute("src")


filename = src.split("/")[-1]
print(filename)

driver.quit()
