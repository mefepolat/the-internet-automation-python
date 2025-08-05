import os
from the_internet_automation.pages.file_upload_page import FileUploadPage

def test_file_upload(driver):
    page = FileUploadPage(driver)
    page.load()

    # Prepare file path (use absolute path for Docker compatibility)

    test_file_path = os.path.abspath("test_data/sample.txt")

    page.upload_file(test_file_path)

    assert page.is_success_message_displayed()
    assert page.get_uploaded_file_name() == "sample.txt"