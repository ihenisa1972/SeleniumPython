import os
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
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


class ParentClass(unittest.TestCase):
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
        self.driver.get(EnvironmentSettings.url)

    def select_nfl(self):
        try:
            self.driver.find_element_by_xpath("/html/body/div[6]/div[2]/header/nav[1]/ul/li[1]/a/span/span[1]")
            self.driver.find_element_by_xpath(
                "/html/body/div[6]/div[2]/header/nav[1]/ul/li[1]/div/ul[1]/li[2]/a/span/span[1]"
            )
        except NoSuchElementException:
            pass

    def select_nba(self):
        try:
           pass
        except NoSuchElementException:
            pass

    def select_ncaaf(self):
        try:
           pass
        except NoSuchElementException:
            pass

    def select_ncaam(self):
        try:
           pass
        except NoSuchElementException:
            pass

    # Test assertions below

    def test_select_nfl(self):
        self.select_nfl()

    '''def test_select_nba(self):
        self.select_nba()

    def test_select_ncaaf(self):
        self.select.ncaaf()

    def test_select_ncaam(self):
        self.select_ncaam()'''

    def tearDown(self):
        # clean up
        self.driver.quit()


if __name__ == '__main__':
    # Run all test functions with HtmlTestRunner to generate html test report.
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=EnvironmentSettings.html_report_dir))

