from selenium.webdriver.common.by import By
from BMRC_Framework_New.pages.base_page import BasePage
class Bmrc_Page(BasePage):

    english = (By.XPATH, "//span[.='English']")
    from_dd = (By.XPATH, "(//select[@class='form-control select fare-selects'])[1]")
    to_dd = (By.XPATH, "(//select[@class='form-control select fare-selects'])[2]")
    get_details = (By.XPATH, "//button[text()='GET Details']")

    def click_english(self):
        self.click(self.english)

    def select_from(self, station):
        self.select_visible_text(self.from_dd, station)

    def select_to(self, station):
        self.select_value(self.to_dd, station)

    def click_get_details(self):
        self.click(self.get_details)