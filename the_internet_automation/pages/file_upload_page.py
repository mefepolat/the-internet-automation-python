from selenium.webdriver.common.by import By

class FileUploadPage:
    URL = "https://the-internet.herokuapp.com/upload"

    def __init__(self, driver):
        self.driver = driver

    # Locators

    FILE_INPUT = (By.ID, "file-upload")
    UPLOAD_BUTTON = (By.ID, "file-submit")
    UPLOADED_FILES = (By.ID, "uploaded-files")
    SUCCESS_MESSAGE = (By.TAG_NAME, "h3") # File Uploaded

    # Actions

    def load(self):
        self.driver.get(self.URL)

    def upload_file(self, file_path):
        self.driver.find_element(*self.FILE_INPUT).send_keys(file_path)
        self.driver.find_element(*self.UPLOAD_BUTTON).click()

    def get_uploaded_file_name(self):
        return self.driver.find_element(*self.UPLOADED_FILES).text

    def is_success_message_displayed(self):
        return "File Uploaded!" in self.driver.find_element(*self.SUCCESS_MESSAGE).text
    
