import configparser

def readLocData(section, key):
    config = configparser.ConfigParser()
    ##G:\framework_setup\locators_testdata\locator.cfg
    config.read("G:/framework_setup/locators_testdata/locator.cfg")
    return config.get(section, key)


print('Locators', 'first_name')