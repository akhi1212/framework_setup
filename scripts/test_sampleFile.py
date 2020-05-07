import pytest
from locators_testdata import locatorReader
from selenium import webdriver
from utitlity.testFixtures import startbrowser

@pytest.mark.usefixtures("startbrowser")
class TestSampple:
    def test_Validatecall(self):
        read_data_firstName = locatorReader.readLocData('Locators', 'Sign_In')
        print(read_data_firstName)
        self.driver.find_element_by_xpath(read_data_firstName).click()
        read_data_lastName = locatorReader.readLocData('Locators', 'last_name')
        print(read_data_lastName)
        gettitle = self.driver.title
        print(gettitle)

