import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
import os

from selenium.webdriver.chrome.service import Service

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")  # for headless mode
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.binary_location = "/usr/bin/chromium"

    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)


    yield driver
    driver.quit()