import os
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import HtmlTestRunner
import xmlrunner
import time
from datetime import date
from datetime import time
from datetime import datetime
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import EnvironmentSettings

# create a unique directory for screenshots
today = datetime.now()
workingdir = "LookupSample_" + today.strftime("%c")
workingdir = workingdir.replace(" ", "_")
workingdir = workingdir.replace(":", "_")
screenshot_path = EnvironmentSettings.validation_screenshots + workingdir
os.mkdir(EnvironmentSettings.validation_screenshots + workingdir)


class LookupSample(unittest.TestCase):
    # load specific driver
    # Chrome and Firefox drivers supported so far
    # TODO: All support for other browsers (IE and Edge)
    # TODO: Add support for test and dev web sites.
    def setUp(self):
        if EnvironmentSettings.browser.lower() == "chrome".lower():
            # create a new Chrome session
            self.driver = webdriver.Chrome()

        elif EnvironmentSettings.browser.lower() == "firefox".lower():
            # create a new Firefox session
            self.driver = webdriver.Firefox()

        elif EnvironmentSettings.browser.lower() == "IE".lower():
            # create a new IE session
            self.driver = webdriver.ie()

        self.driver.implicitly_wait(60)
        self.driver.maximize_window()
        self.driver.get("https://uat-bioinventory.biostorage.com")

    # step1:
    # Navigate to https://uat-bioinventory.biostorage.com
    def step1_navigate_to_site(self):
        # this step is handled with the setUp() method.
        pass

    # step2:
    # Input username: web_user and password: Sample123 and click Login
    def step2_login(self):
        # username
        username = self.driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr/td/div/div[1]/input")
        username.send_keys(EnvironmentSettings.user_name)

        # password
        password = self.driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr/td/div/div[2]/input")
        password.send_keys(EnvironmentSettings.password)

        # click login button
        login_button = self.driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr/td/div/div[4]/div[1]")
        login_button.click()

    # step3: Click within the search field next to the user links and input 'A177BC106-001' and press enter
    def step3_Search(self):
        # login
        self.step2_login()

        # insert 'A177BC106-001' into search box
        search = self.driver.find_element_by_xpath("/html/body/form/div[6]/div/div[2]/div[1]/input")
        search.send_keys("A177BC106-001")

        # press enter
        search.send_keys(Keys.ENTER)

    # step4: Click Sample Info button in the Site Navigation menu
    def step4_click_sample_button(self):
        # login
        self.step2_login()

        # click sample button
        sample_button = self.driver.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div/div[2]/div")
        sample_button.click()

    # step5: Click within each of the search options (Except Box Search), using the same sample identifier
    def step5_click_search_options(self):
        # login
        self.step2_login()

        # click sample button
        sample_button = self.driver.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div/div[2]/div")
        sample_button.click()

    # step6: From the Sample Info page,
    # click the link in the subheader text "Search Page" to search from the main search page
    def step6_click_search_page(self):
        # login
        self.step2_login()

        # click sample button
        sample_button = self.driver.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div/div[2]/div")
        sample_button.click()

        # click search page link
        search_page_link = self.driver.find_element_by_xpath("/html/body/form/div[8]/div/div/a")
        search_page_link.click()

    # step7: Input the sample identifier and click New Search
    def step7_input_sample_identifier_click_new_search(self):
        # login
        self.step2_login()

        # click sample button
        sample_button = self.driver.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div/div[2]/div")
        sample_button.click()

        # click search page link
        search_page_link = self.driver.find_element_by_xpath("/html/body/form/div[8]/div/div/a")
        search_page_link.click()

        # enter sample identifier
        sample_identifier_search = self.driver.find_element_by_xpath(
            "/html/body/form/div[8]/div[2]/div/div/div[1]/div[1]/div[1]/input[1]")
        sample_identifier_search.send_keys("A177BC106-001")

        # click new search
        new_search_button = self.driver.find_element_by_xpath(
            "/html/body/form/div[8]/div[2]/div/div/div[1]/div[1]/div[1]/input[2]")
        new_search_button.click()

    # step8: Click the Sample Info button in the Site Navigation menu,
    # click within the Box Samples search field,  type in '563126', and press enter
    def step8_click_sample_info_button(self):
        # login
        self.step2_login()

        # click sample info button
        sample_info_button = self.driver.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div/div[2]/img")
        sample_info_button.click()

        # click with box samples search field, enter '563126', press enter
        box_samples_field = self.driver.find_element_by_xpath(
            "/html/body/form/div[8]/div/table/tbody/tr[3]/td/div/div/div/input[1]")
        box_samples_field.send_keys("563126")

        # press enter
        box_samples_field.send_keys(Keys.ENTER)

    # step9: Click Sign Out
    def step9_sign_out(self):
        # login
        self.step2_login()

        sign_out = self.driver.find_element_by_xpath(
            "/html/body/form/div[6]/div/div[2]/div[3]/div[1]/a")
        sign_out.click()

    def test_step1_navigate_to_site(self):
        self.step1_navigate_to_site()
        # scroll down to bottom of page to get screen shot
        self.scroll_to_bottom_page()

        try:
            # login page displays (BioInventory banner)
            banner = self.driver.find_element_by_xpath("/html/body/form/div[3]/img")
            self.driver.save_screenshot(screenshot_path + "\\Step1_banner.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find BioInventory banner")
            self.driver.save_screenshot(screenshot_path + "\\Step1_banner.png")
            self.tearDown()

        try:
            # username edit box displays
            username = self.driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr/td/div/div[1]/input")
            self.driver.save_screenshot(screenshot_path + "\\Step1_username.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find username login edit box")
            self.driver.save_screenshot(screenshot_path + "\\Step1_username.png")
            self.tearDown()

        try:
            # password edit box displays.
            self.driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr/td/div/div[2]/input")
            self.driver.save_screenshot(screenshot_path + "\\Step1_password.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find password login edit box")
            self.driver.save_screenshot(screenshot_path + "\\Step1_password.png")
            self.tearDown()

        try:
            # link to reset username is displayed.
            self.driver.find_element_by_xpath(
                "/html/body/form/div[3]/table/tbody/tr/td/div/div[3]/a[1]")
            self.driver.save_screenshot(screenshot_path + "\\Step1_reset_username_link.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find reset password link")
            self.driver.save_screenshot(screenshot_path + "\\Step1_reset_username_link.png")
            self.tearDown()

        try:
            # link to reset password is displayed.
            self.driver.find_element_by_xpath(
                "/html/body/form/div[3]/table/tbody/tr/td/div/div[3]/a[2]")
            self.driver.save_screenshot(screenshot_path + "\\Step1_reset_password_link.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find reset password link")
            self.driver.save_screenshot(screenshot_path + "\\Step1_reset_password_link.png")
            self.tearDown()

        try:
            # login button is displayed.
            self.driver.find_element_by_xpath(
                "/html/body/form/div[3]/table/tbody/tr/td/div/div[4]/div[1]")
            self.driver.save_screenshot(screenshot_path + "\\Step1_login_button.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find login button")
            self.driver.save_screenshot(screenshot_path + "\\Step1_login_button.png")
            self.tearDown()

    # expected results2
    def test_step2_login(self):
        self.step2_login()

        try:
            self.driver.find_element_by_xpath("/html/body/form/div[5]/div[1]/div/a/img")
            self.driver.save_screenshot(screenshot_path + "\\Step2_banner_icon.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find Brooks Life Sciences banner")
            self.driver.save_screenshot(screenshot_path + "\\Step2_banner_icon.png")
            self.tearDown()

        try:
            self.driver.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div/div[1]/img")
            self.driver.save_screenshot(screenshot_path + "\\Step2_bioinventory_icon.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find BioInventory menu item")
            self.driver.save_screenshot(screenshot_path + "\\Step2_bioinventory_icon.png")
            self.tearDown()

        try:
            self.driver.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div/div[2]/img")
            self.driver.save_screenshot(screenshot_path + "\\Step2_sample_info_icon.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find Sample Info menu item")
            self.driver.save_screenshot(screenshot_path + "\\Step2_sample_info_icon.png")
            self.tearDown()

        try:
            self.driver.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div/div[3]/img")
            self.driver.save_screenshot(screenshot_path + "\\Step2_transport_icon.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find Transport menu item")
            self.driver.save_screenshot(screenshot_path + "\\Step2_transport_icon.png")
            self.tearDown()

        try:
            self.driver.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div/div[4]/img")
            self.driver.save_screenshot(screenshot_path + "\\Step2_reports_icon.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find Reports menu item")
            self.driver.save_screenshot(screenshot_path + "\\Step2_reports_icon.png")
            self.tearDown()

        try:
            self.driver.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div/div[5]/img")
            self.driver.save_screenshot(screenshot_path + "\\Step2_disposal_icon.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find Disposal menu item")
            self.driver.save_screenshot(screenshot_path + "\\Step2_disposal_icon.png")
            self.tearDown()

        try:
            self.driver.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div/div[6]/img")
            self.driver.save_screenshot(screenshot_path + "\\Step2_lab_services_icon.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find Lab Services menu item")
            self.driver.save_screenshot(screenshot_path + "\\Step2_lab_services_icon.png")
            self.tearDown()

        try:
            self.driver.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div/div[7]/img")
            self.driver.save_screenshot(screenshot_path + "\\Step2_bio_insight_icon.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find Bio Insight menu item")
            self.driver.save_screenshot(screenshot_path + "\\Step2_bio_insight_icon.png")
            self.tearDown()

        try:
            self.driver.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div/div[8]/img")
            self.driver.save_screenshot(screenshot_path + "\\Step2_help_icon.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find Help menu item")
            self.driver.save_screenshot(screenshot_path + "\\Step2_help_icon.png")
            self.tearDown()

        try:
            self.driver.find_element_by_xpath("/html/body/form/div[6]/div/div[2]/div[3]/div[1]/a")
            self.driver.save_screenshot(screenshot_path + "\\Step2_sign_out_link.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find Sign Out menu item")
            self.driver.save_screenshot(screenshot_path + "\\Step2_sign_out_link.png")
            self.tearDown()

        try:
            self.driver.find_element_by_xpath("/html/body/form/div[6]/div/div[2]/div[3]/div[3]/a")
            self.driver.save_screenshot(screenshot_path + "\\Step2_my_account_link.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find My Account menu item")
            self.driver.save_screenshot(screenshot_path + "\\Step2_my_account_link.png")
            self.tearDown()

        try:
            self.driver.find_element_by_xpath("/html/body/form/div[6]/div/div[2]/div[3]/div[5]/a")
            self.driver.save_screenshot(screenshot_path + "\\Step2_help_link.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find Help menu item")
            self.driver.save_screenshot(screenshot_path + "\\Step2_help_link.png")
            self.tearDown()

    # results3 : Pop-up displays indicating search is processing.
    # Once the sample is found,
    # https://uat-bioinventory.biostorage.com/Secured/Search.aspx?ss=A177BC106-001 page displays
    # TODO: Need to add a check for the search box.
    # TODO: Haven't found way to get handle to dialog box
    def test_step3_Search(self):
        self.step3_Search()

        try:
            self.driver.find_element_by_xpath("/html/body/form/div[8]/div[2]/div/div/div[1]/div[2]/div")
            self.driver.save_screenshot(screenshot_path + "\\step3_text_searching.png")
        except NoSuchElementException:
            self.assertTrue(False, "Could not search for sample")
            self.driver.save_screenshot(screenshot_path + "\\step3_text_searching.png")
            self.tearDown()

        try:
            find_sample = self.driver.find_element_by_xpath(
                "/html/body/form/div[8]/div[2]/div/div/div[2]/div[3]/div/table/tbody/tr[2]/td[3]/div")
            self.assertEqual("A177BC106-001", find_sample.text)
            self.driver.save_screenshot(screenshot_path + "\\step3_text_searching.png")
        except NoSuchElementException:
            self.assertTrue(False, "Could not search for sample")
            self.driver.save_screenshot(screenshot_path + "\\step3_text_searching.png")
            self.tearDown()

    # results4: Click Sample Info button in the Site Navigation menu
    def test_step4_click_sample_button(self):
        self.step4_click_sample_button()

        try:
            self.driver.find_element_by_xpath("/html/body/form/div[8]/div/h2[2]")
            self.driver.save_screenshot(screenshot_path + "\\step4_sample_info_text.png")
        except NoSuchElementException:
            self.assertTrue(False, "Sample Info page not displayed")
            self.driver.save_screenshot(screenshot_path + "\\step4_sample_info_text.png")
            self.tearDown()

    # results5: Click within each of the search options (Except Box Search), using the same sample identifier
    def test_step5_click_search_options(self):
        self.step5_click_search_options()

        try:
            # sample demographics
            sample_demographics = self.driver.find_element_by_xpath(
                "/html/body/form/div[8]/div/table/tbody/tr[1]/td[1]/div/div/div/input[1]")
            sample_demographics.send_keys("A177BC106-001")

            # press enter
            sample_demographics.send_keys(Keys.ENTER)
            self.driver.save_screenshot(screenshot_path + "\\step5_sample_demographics.png")

            # go back one screen
            self.driver.back()
        except NoSuchElementException:
            self.assertTrue(False, "Sample demographic not found")
            self.driver.save_screenshot(screenshot_path + "\\step5_sample_demographics.png")
            self.tearDown()

        try:
            # sample moves
            sample_moves = self.driver.find_element_by_xpath(
                "/html/body/form/div[8]/div/table/tbody/tr[2]/td[1]/div/div/div/input[1]")
            sample_moves.send_keys("A177BC106-001")

            # press enter
            sample_moves.send_keys(Keys.ENTER)
            self.driver.save_screenshot(screenshot_path + "\\step5_sample_moves.png")

            # go back one screen
            self.driver.back()
        except NoSuchElementException:
            self.assertTrue(False, "Sample moves not found")
            self.driver.save_screenshot(screenshot_path + "\\step5_sample_moves.png")
            self.tearDown()

        try:
            # sample history
            sample_history = self.driver.find_element_by_xpath(
                "/html/body/form/div[8]/div/table/tbody/tr[1]/td[2]/div/div/div/input[1]")
            sample_history.send_keys("A177BC106-001")

            # press enter
            sample_history.send_keys(Keys.ENTER)
            self.driver.save_screenshot(screenshot_path + "\\step5_sample_history.png")

            # go back one screen
            self.driver.back()
        except NoSuchElementException:
            self.assertTrue(False, "Sample history not found")
            self.driver.save_screenshot(screenshot_path + "\\step5_sample_history.png")
            self.tearDown()

        try:
            # related samples
            related_samples = self.driver.find_element_by_id("ctl00_MainBody_txtSampleRelated")
            related_samples.send_keys("A177BC106-001")

            # press enter
            related_samples.send_keys(Keys.ENTER)
            self.driver.save_screenshot(screenshot_path + "\\step5_related_samples.png")

            # go back one screen
            self.driver.back()
        except NoSuchElementException:
            self.assertTrue(False, "Related samples not found")
            self.driver.save_screenshot(screenshot_path + "\\step5_related_samples.png")
            self.tearDown()

        try:
            # click sample button
            sample_button = self.driver.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div/div[2]/div")
            sample_button.click()
            self.driver.save_screenshot(screenshot_path + "\\step5_sample_button.png")
        except NoSuchElementException:
            self.assertTrue(False, "Sample button not found")
            self.driver.save_screenshot(screenshot_path + "\\step5_sample_button.png")
            self.tearDown()

    # results6 : From the Sample Info page,
    # click the link in the subheader text "Search Page" to search from the main search page
    def test_step6_click_search_page(self):
        self.step6_click_search_page()

        try:
            self.driver.find_elements_by_id("ctl00_MainBody_upSearchResults")
            self.driver.save_screenshot(screenshot_path + "\\step6_click_search_page.png")
        except NoSuchElementException:
            self.assertTrue(False, "Search page not found")
            self.driver.save_screenshot(screenshot_path + "\\step6_click_search_page.png")
            self.tearDown()

    # results7: Input the sample identifier and click New Search
    def test_step7_input_sample_identifier_click_new_search(self):
        self.step7_input_sample_identifier_click_new_search()

        try:
            self.driver.find_element_by_xpath(
                "/html/body/form/div[8]/div[2]/div/div/div[2]/div[3]/div/table/tbody/tr[2]/td[3]/div")
            self.driver.save_screenshot(screenshot_path + "\\step7_input_sample_identifier.png")
        except NoSuchElementException:
            self.assertTrue(False, "Sample not found")
            self.driver.save_screenshot(screenshot_path + "\\step7_input_sample_identifier.png")
            self.tearDown()

    # results8: Click the Sample Info button in the Site Navigation menu,
    # click within the Box Samples search field,  type in '563126', and press enter
    def test_step8_click_sample_info_button(self):
        self.step8_click_sample_info_button()

        try:
            self.driver.find_element_by_xpath(
                "/html/body/form/div[8]/div[2]/div/div/div[2]/div[3]/div/table/tbody/tr[2]/td[2]/div/input")
            self.driver.save_screenshot(screenshot_path + "\\step8_click_sample_info_button.png")
        except NoSuchElementException:
            self.assertTrue(False, "No samples found")
            self.driver.save_screenshot(screenshot_path + "\\step8_click_sample_info_button.png")
            self.tearDown()

    # results9: Click Sign Out
    def test_step9_sign_out(self):
        self.step9_sign_out()
        # scroll down to bottom of page to get screen shot
        self.scroll_to_bottom_page()

        try:
            # login page displays (BioInventory banner)
            self.driver.find_element_by_xpath("/html/body/form/div[3]/img")
            self.driver.save_screenshot(screenshot_path + "\\step9_click_sign_out.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find BioInventory banner")
            self.driver.save_screenshot(screenshot_path + "\\step9_click_sign_out.png")
            self.tearDown()

    def tearDown(self):
        # clean up
        self.driver.quit()

    # helper functions below
    def scroll_to_bottom_page(self):
        self.driver.execute_script("window.scrollTo(0, 1080)")
    # helper functions above


if __name__ == '__main__':
    # Run all test functions with HtmlTestRunner to generate html test report.
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=EnvironmentSettings.html_report_dir))
