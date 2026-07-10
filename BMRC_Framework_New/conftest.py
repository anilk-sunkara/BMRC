import pytest
from selenium import webdriver

@pytest.fixture
def setup():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("https://www.bmrc.co.in/")

    yield driver

    driver.quit()