import pytest
from locators_testdata import locatorReader
from selenium import webdriver
from utitlity.testFixtures import startbrowser

@pytest.mark.usefixtures("startbrowser")
class TestSampple:
    def test_Validatecall(self):
        read_data_sin = locatorReader.readLocData('Locators', 'Sign_In')
        print(read_data_sin)
        self.driver.find_element_by_xpath(read_data_sin).click()
        read_usr = locatorReader.readLocData('Locators', 'user_name')
        self.driver.find_element_by_xpath(read_usr).send_keys("admin")
        read_data_pass = locatorReader.readLocData('Locators', 'passwd')
        self.driver.find_element_by_xpath(read_data_pass).send_keys("admin")
        bttn_clk = locatorReader.readLocData('Locators', 'bttn')
        self.driver.find_element_by_xpath(bttn_clk).click()
        print(read_data_pass)
        gettitle = self.driver.title
        print(gettitle)

