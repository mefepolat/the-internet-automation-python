from the_internet_automation.pages.dynamic_controls_page import DynamicControlsPage

def test_input_enable_disable(driver):
    page = DynamicControlsPage(driver)
    page.load()

    # Click "Enable" and wait for input to become enabled
    page.click_enable_disable_button()
    page.wait_for_input_enabled()
    assert page.is_input_enabled(), "Input should be enabled"

    # Type into input
    page.type_into_input("Testing the input")

    # Click "Disable" and wait for input to become disabled

    page.click_enable_disable_button()
    page.wait_for_input_disabled()
    assert not page.is_input_enabled(), "Input should be disabled"