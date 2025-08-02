import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")  # for headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    yield driver
    driver.quit()