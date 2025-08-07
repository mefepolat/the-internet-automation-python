from selenium.webdriver.common.by import By

class DragAndDropPage:
    URL = "https://the-internet.herokuapp.com/drag_and_drop"


    # Locators

    COLUMN_A = (By.ID, "column-a")
    COLUMN_B = (By.ID, "column-b")
    HEADER_A = (By.CSS_SELECTOR, "#column-a header")
    HEADER_B = (By.CSS_SELECTOR, "#column-b header")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)


    def get_column_a_header(self):
        return self.driver.find_element(*self.HEADER_A).text

    def get_column_b_header(self):
        return self.driver.find_element(*self.HEADER_B).text

    def drag_a_to_b(self):
        with open("the_internet_automation/helpers/drag_and_drop_helper.js", "r") as js_file:
            drag_and_drop_script = js_file.read()
        source = self.driver.find_element(*self.COLUMN_A)
        target = self.driver.find_element(*self.COLUMN_B)
        self.driver.execute_script(drag_and_drop_script, source, target)
