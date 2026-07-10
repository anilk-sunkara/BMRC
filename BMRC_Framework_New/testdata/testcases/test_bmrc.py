import pytest
from BMRC_Framework_New.pages.bmrc_page import Bmrc_Page
from BMRC_Framework_New.utilities.excel_reader import ExcelReader
data = ExcelReader.get_data()

@pytest.mark.parametrize("from_station,to_station", data)
def test_bmrc(setup, from_station, to_station):

    driver = setup

    bmrc = Bmrc_Page(driver)

    bmrc.click_english()

    bmrc.select_from(from_station)

    bmrc.select_to(to_station)

    bmrc.click_get_details()