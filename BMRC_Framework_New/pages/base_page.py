from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def select_visible_text(self, locator, text):

    dropdown = WebDriverWait(self.driver,20).until(
        EC.presence_of_element_located(locator)
    )

    select = Select(dropdown)

    # Try exact match first
    try:
        select.select_by_visible_text(text)
        return
    except:
        pass

    # Try partial match
    for option in select.options:
        if text.lower() in option.text.lower():
            option.click()
            return

    raise Exception(f"{text} not found in dropdown")