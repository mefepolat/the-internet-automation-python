from the_internet_automation.pages.login_page import LoginPage

def test_valid_login(driver):
    page = LoginPage(driver)
    page.load()
    page.login("tomsmith", "SuperSecretPassword!")
    assert page.is_success_message_displayed()

def test_invalid_login(driver):
    page = LoginPage(driver)
    page.load()
    page.login("invalid_user", "invalid_pass")
    assert page.is_error_message_displayed()