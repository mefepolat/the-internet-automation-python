from selenium.webdriver.common.by import By


class CheckboxPage:
    URL = "https://the-internet.herokuapp.com/checkboxes"

    def __init__(self, driver):
        self.driver = driver


    CHECKBOX1 = (By.XPATH, "//form[@id='checkboxes']/input[1]")
    CHECKBOX2 = (By.XPATH, "//form[@id='checkboxes']/input[2]")

    def load(self):
        self.driver.get(self.URL)

    def is_checkbox_selected(self, checkbox_locator):
        return self.driver.find_element(*checkbox_locator).is_selected()

    def toggle_checkbox(self, checkbox_locator):
        self.driver.find_element(*checkbox_locator).click()