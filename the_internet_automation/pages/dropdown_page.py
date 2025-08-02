from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class DropdownPage:
    URL = "https://the-internet.herokuapp.com/dropdown"

    def __init__(self, driver):
        self.driver = driver


    # Locator
    DROPDOWN = (By.ID, "dropdown")

    def load(self):
        self.driver.get(self.URL)

    def select_option_by_text(self, visible_text):
        dropdown = Select(self.driver.find_element(*self.DROPDOWN))
        dropdown.select_by_visible_text(visible_text)

    def get_selected_option(self):
        dropdown = Select(self.driver.find_element(*self.DROPDOWN))
        return dropdown.first_selected_option.text