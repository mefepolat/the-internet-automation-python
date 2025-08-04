from the_internet_automation.pages.checkbox_page import CheckboxPage

def test_toggle_checkboxes(driver):
    page = CheckboxPage(driver)
    page.load()

    # Toggle checkbox 1
    initial_1 = page.is_checkbox_selected(page.CHECKBOX1)
    page.toggle_checkbox(page.CHECKBOX1)
    assert page.is_checkbox_selected(page.CHECKBOX1) != initial_1

    # Toggle checkbox 2
    initial_2 = page.is_checkbox_selected(page.CHECKBOX2)
    page.toggle_checkbox(page.CHECKBOX2)
    assert page.is_checkbox_selected(page.CHECKBOX2) != initial_2
