from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, driver):
        self.driver = driver


    # Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.radius")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".flash.success")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".flash.error")

    #Actions

    def load(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def is_success_message_displayed(self):
        try:
            element = self.driver.find_element(*self.SUCCESS_MESSAGE)
            return "You logged into a secure area!" in element.text
        except NoSuchElementException:
            return False

    def is_error_message_displayed(self):
        try:
            error_element = self.driver.find_element(*self.ERROR_MESSAGE)
            return "your username is invalid!" in error_element.text.lower()
        except NoSuchElementException:
            return False