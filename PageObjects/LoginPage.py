import os

import HtmlTestRunner
from datetime import datetime
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from Environment import EnvironmentSettings

# create a unique directory for screenshots
today = datetime.now()
workingdir = "LogInLogOut_" + today.strftime("%c")
workingdir = workingdir.replace(" ", "_")
workingdir = workingdir.replace(":", "_")
screenshot_path = EnvironmentSettings.validation_screenshots + workingdir
os.mkdir(EnvironmentSettings.validation_screenshots + workingdir)


class LoginPage(unittest.TestCase):
    def setUp(self):
        # load specific driver
        # Chrome and Firefox drivers supported so far
        # TODO: All support for other browsers (IE and Edge)
        # TODO: Add support for test and dev web sites.
        if EnvironmentSettings.browser.lower() == "chrome".lower():
            # create a new Chrome session
            self.driver = webdriver.Chrome()

        elif EnvironmentSettings.browser.lower() == "firefox".lower():
            # create a new Firefox session
            self.driver = webdriver.Firefox()

        elif EnvironmentSettings.browser.lower() == "IE".lower():
            # create a new IE session
            self.driver = webdriver.ie()

        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(EnvironmentSettings.web_site_address)

    def login(self):
        pass

    def test_login(self):
        pass

    def tearDown(self):
        # clean up
        self.driver.quit()


if __name__ == '__main__':
    # Run all test functions with HtmlTestRunner to generate html test report.
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=EnvironmentSettings.html_report_dir))