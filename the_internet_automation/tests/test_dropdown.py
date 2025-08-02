from the_internet_automation.pages.dropdown_page import DropdownPage

def test_select_option(driver):
    page = DropdownPage(driver)
    page.load()
    page.select_option_by_text("Option 2")
    assert page.get_selected_option() == "Option 2"