from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def select_visible_text(self, locator, text):
        Select(self.driver.find_element(*locator)).select_by_visible_text(text)

    def select_value(self, locator, value):
        Select(self.driver.find_element(*locator)).select_by_value(value)