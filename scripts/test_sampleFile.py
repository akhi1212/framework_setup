import pytest
from locators_testdata import locatorReader
from locators_testdata import configReader
import os
from selenium import webdriver
from utitlity.testFixtures import startbrowser


@pytest.mark.usefixtures("startbrowser")
def test_Validatecall(startbrowser):
    read_data_firstName = locatorReader.readLocData('Locators', 'first_name')
    print(read_data_firstName)
    read_data_lastName = locatorReader.readLocData('Locators', 'last_name')
    print(read_data_lastName)
    gettitle = driver.title
    print(gettitle)

