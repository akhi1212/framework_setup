import pytest
from locators_testdata import locatorReader
from selenium import webdriver
from utitlity.testFixtures import startbrowser
import logging

@pytest.mark.usefixtures("startbrowser")
class TestSampple:
    def test_Validatecall(self):
        log = logging.getLogger('test_Validatecall')
        read_data_sin = locatorReader.readLocData('Locators', 'Sign_In')
        print(read_data_sin)
        self.driver.find_element_by_xpath(read_data_sin).click()
        log.debug('click sign in button')
        read_usr = locatorReader.readLocData('Locators', 'user_name')
        self.driver.find_element_by_xpath(read_usr).send_keys("admin")
        log.debug('locate and enter username ')
        read_data_pass = locatorReader.readLocData('Locators', 'passwd')
        self.driver.find_element_by_xpath(read_data_pass).send_keys("admin")
        log.debug('locate and enter passwod ')
        bttn_clk = locatorReader.readLocData('Locators', 'bttn')
        self.driver.find_element_by_xpath(bttn_clk).click()
        log.debug('locate button and click button  ')
        print(read_data_pass)
        gettitle = self.driver.title
        print("The title of webpage is : " +gettitle)
        log.debug('title of the page is :')

