from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def select_visible_text(self, locator, text):

        dropdown = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(locator)
        )

        select = Select(dropdown)

        print("\nAvailable options:")
        for option in select.options:
            print(repr(option.text))

        select.select_by_visible_text(text.strip())

    def select_value(self, locator, value):

        dropdown = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(locator)
        )

        Select(dropdown).select_by_value(value)