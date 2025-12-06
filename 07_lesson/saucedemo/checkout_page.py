from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, value):
        self.driver.find_element(By.ID, "first-name").send_keys(value)

    def enter_last_name(self, value):
        self.driver.find_element(By.ID, "last-name").send_keys(value)

    def enter_zip(self, value):
        self.driver.find_element(By.ID, "postal-code").send_keys(value)

    def click_continue(self):
        self.driver.find_element(By.ID, "continue").click()

    def get_total(self):
        return self.driver.find_element(
            By.CLASS_NAME,
            "summary_total_label"
        ).text
