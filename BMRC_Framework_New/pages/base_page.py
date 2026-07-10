from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def select_visible_text(self, locator, text):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )

        select = Select(dropdown)

        for option in select.options:
            if option.text.strip().lower() == text.strip().lower():
                select.select_by_visible_text(option.text)
                return

        raise Exception(f"'{text}' not found in dropdown")

    def select_value(self, locator, value):
        Select(self.driver.find_element(*locator)).select_by_value(value)