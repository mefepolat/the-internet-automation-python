from the_internet_automation.pages.drag_and_drop_page import DragAndDropPage


def test_drag_and_drop(driver):
    page = DragAndDropPage(driver)
    page.load()

    before_a = page.get_column_a_header()
    before_b = page.get_column_b_header()

    page.drag_a_to_b()

    after_a = page.get_column_a_header()
    after_b = page.get_column_b_header()

    assert before_a != after_a
    assert before_b != after_b
