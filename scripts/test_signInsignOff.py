import pytest
from locators_testdata import locatorReader
from utitlity.testFixtures import startbrowser
import  time

@pytest.mark.usefixtures("startbrowser")
class TestPers:
    def test_Validatepersonal(self):
        per = locatorReader.readLocData('Locators', 'online')
        self.driver.find_element_by_xpath(per).click()
        read_usr = locatorReader.readLocData('Locators', 'user_name')
        self.driver.find_element_by_xpath(read_usr).send_keys("admin")
        read_data_pass = locatorReader.readLocData('Locators', 'passwd')
        self.driver.find_element_by_xpath(read_data_pass).send_keys("admin")
        bttn_clk = locatorReader.readLocData('Locators', 'bttn')
        self.driver.find_element_by_xpath(bttn_clk).click()
        time.sleep(10)
        sign_off = locatorReader.readLocData('Locators','sign_off')
        self.driver.find_element_by_xpath(sign_off).click()
