from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DynamicControlsPage:
    URL = "https://the-internet.herokuapp.com/dynamic_controls"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators

    ENABLE_DISABLE_BUTTON = (By.CSS_SELECTOR, "#input-example button")
    INPUT_FIELD = (By.CSS_SELECTOR, "#input-example input")
    MESSAGE = (By.ID, "message")

    # Actions

    def load(self):
        self.driver.get(self.URL)

    def click_enable_disable_button(self):
        self.driver.find_element(*self.ENABLE_DISABLE_BUTTON).click()

    def wait_for_input_enabled(self):
        self.wait.until(EC.element_to_be_clickable(self.INPUT_FIELD))

    def wait_for_input_disabled(self):
        self.wait.until(lambda driver: not driver.find_element(*self.INPUT_FIELD).is_enabled())

    def type_into_input(self, text):
        self.driver.find_element(*self.INPUT_FIELD).send_keys(text)

    def is_input_enabled(self):
        return self.driver.find_element(*self.INPUT_FIELD).is_enabled()