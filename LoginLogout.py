import os
import unittest
import time

import HtmlTestRunner
from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
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
workingdir = "LogInLogOut_" + today.strftime("%c")
workingdir = workingdir.replace(" ", "_")
workingdir = workingdir.replace(":", "_")
screenshot_path = EnvironmentSettings.validation_screenshots + workingdir
os.mkdir(EnvironmentSettings.validation_screenshots + workingdir)


class LoginLogout(unittest.TestCase):

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
        self.driver.get("https://uat-bioinventory.biostorage.com")

    # step1:
    # Navigate to https://uat-bioinventory.biostorage.com
    def navigate_to_site(self):
        # this step is handled with the setUp() method.
        pass

    # step2:
    # Input username: web_user and password:
    def login(self):
        # username
        username = self.driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr/td/div/div[1]/input")
        username.send_keys(EnvironmentSettings.user_name)

        # password
        password = self.driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr/td/div/div[2]/input")
        password.send_keys(EnvironmentSettings.password)

        # click login button
        login_button = self.driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr/td/div/div[4]/div[1]")
        login_button.click()

    # step3:
    # Click Sign Out
    def sign_out(self):
        logout = self.driver.find_element_by_xpath("/html/body/form/div[6]/div/div[2]/div[3]/div[1]/a")
        logout.click()

    # step4:
    # Click LOGIN
    def click_login(self):
        login = self.driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr/td/div/div[4]/div[1]")
        login.click()

    # step5:
    # Input invalid username and password
    def input_invalid_username_password(self):
        invalid_username = self.driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr/td/div/div[1]/input")
        invalid_username.send_keys(EnvironmentSettings.fake_user_name)

        valid_password = self.driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr/td/div/div[2]/input")
        valid_password.send_keys(EnvironmentSettings.fake_password)

    # step6:
    # Input valid username and incorrect password
    def input_valid_username_invalid_password(self):
        valid_username = self.driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr/td/div/div[1]/input")
        valid_username.send_keys(EnvironmentSettings.user_name)

        invalid_password = self.driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr/td/div/div[2]/input")
        invalid_password.send_keys(EnvironmentSettings.fake_password)

    # step7:
    # Click the "Forgot your username?" link
    def click_forget_your_username_link(self):
        forget_username_link = self.driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr/td/div/div[3]/a[1]")
        forget_username_link.click()

    # step8:
    # Click back on browser
    def click_back_on_browser(self):
        self.click_forget_your_username_link()
        self.driver.back()

    # step9:
    # click the "forgot your password?" link
    def click_forgot_your_password(self):
        forget_password_link = self.driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr/td/div/div[3]/a[2]")
        forget_password_link.click()

    # implementation of assertions
    # expected results1:
    def test_Step1_navigate_to_site(self):
        # log in page displays (BioInventory banner displays)

        try:
            self.assertTrue(self.driver.find_element_by_xpath("//*[@id='imgBioInsightLogo']"),
                            "Log in page displays")
            self.driver.save_screenshot(screenshot_path + "\\Step1_BioInventoryBanner.png")
        except NoSuchElementException:
            self.assertTrue(False, "Log in page did not display")
            self.driver.save_screenshot(screenshot_path + "\\Step1_BioInventoryBanner.png")
            self.tearDown()

        # fields to input username and password
        try:
            self.assertTrue(
                self.driver.find_element_by_xpath("//*[@id='lgvLoginView_lgLogin_UserName']"),
                "Field to input username found")
            self.driver.save_screenshot(screenshot_path + "\\Step1_UserName_Edit_Box.png")
        except NoSuchElementException:
            self.assertTrue(False, "Field to input username not found")
            self.driver.save_screenshot(screenshot_path + "\\Step1_UserName_Edit_Box.png")
            self.tearDown()

        try:
            self.assertTrue(
                self.driver.find_element_by_xpath("//*[@id='lgvLoginView_lgLogin_Password']"),
                "Field to input password found")
            self.driver.save_screenshot(screenshot_path + "\\Step1_ScreenshotsPassword_Edit_Box.png")
        except NoSuchElementException:
            self.assertTrue(False, "Field to input password not found")
            self.driver.save_screenshot(screenshot_path + "\\Step1_ScreenshotsPassword_Edit_Box.png")
            self.tearDown()

        # links to reset username and password
        try:
            self.assertTrue(
                self.driver.find_element_by_xpath("//*[@id='lgvLoginView_lgLogin']/tbody/tr/td/div/div[3]/a[1]"),
                "Link to reset username found")
            self.driver.save_screenshot(screenshot_path + "\\Step1_ScreenshotsUserName_Rest_Link.png")
        except NoSuchElementException:
            self.assertTrue(False, "Link to reset username not found")
            self.driver.save_screenshot(screenshot_path + "\\Step1_ScreenshotsUserName_Rest_Link.png")
            self.tearDown()

        try:
            self.assertTrue(
                self.driver.find_element_by_xpath("//*[@id='lgvLoginView_lgLogin']/tbody/tr/td/div/div[3]/a[2]"),
                "Link to reset password found")
            self.driver.save_screenshot(screenshot_path + "\\Step1_Password_Rest_Link.png")
        except NoSuchElementException:
            self.assertTrue(False, "Link to reset password not found")
            self.driver.save_screenshot(screenshot_path + "\\Step1_Password_Rest_Link.png")
            self.tearDown()

        # login button
        try:
            self.assertTrue(
                self.driver.find_element_by_xpath("//*[@id='btnLogin']"),
                "Login button found")
            self.driver.save_screenshot(screenshot_path + "\\Step1_ScreenshotsLogin_Button.png")
        except NoSuchElementException:
            self.assertTrue(False, "Login button not found")
            self.driver.save_screenshot(screenshot_path + "\\Step1_ScreenshotsLogin_Button.png")
            self.tearDown()

    # expected results2:
    def test_Step2_login(self):
        self.login()

        try:
            self.driver.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div/div[1]/img")
            self.driver.save_screenshot(screenshot_path + "\\Step2_bioinventory.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find BioInventory menu item")
            self.driver.save_screenshot(screenshot_path + "\\Step2_bioinventory.png")
            self.tearDown()

        try:
            self.driver.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div/div[2]/img")
            self.driver.save_screenshot(screenshot_path + "\\Step2_sample_info.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find Sample Info menu item")
            self.driver.save_screenshot(screenshot_path + "\\Step2_sample_info.png")
            self.tearDown()

        try:
            self.driver.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div/div[3]/img")
            self.driver.save_screenshot(screenshot_path + "\\Step2_transport.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find Transport menu item")
            self.driver.save_screenshot(screenshot_path + "\\Step2_transport.png")
            self.tearDown()

        try:
            self.driver.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div/div[4]/img")
            self.driver.save_screenshot(screenshot_path + "\\Step2_reports.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find Reports menu item")
            self.driver.save_screenshot(screenshot_path + "\\Step2_reports.png")
            self.tearDown()

        try:
            self.driver.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div/div[5]/img")
            self.driver.save_screenshot(screenshot_path + "\\Step2_disposal.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find Disposal menu item")
            self.driver.save_screenshot(screenshot_path + "\\Step2_disposal.png")
            self.tearDown()

        try:
            self.driver.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div/div[6]/img")
            self.driver.save_screenshot(screenshot_path + "\\Step2_lab_services.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find Lab Services menu item")
            self.driver.save_screenshot(screenshot_path + "\\Step2_lab_services.png")
            self.tearDown()

        try:
            self.driver.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div/div[7]/img")
            self.driver.save_screenshot(screenshot_path + "\\Step2_bio_insight.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find Bio Insight menu item")
            self.driver.save_screenshot(screenshot_path + "\\Step2_bio_insight.png")
            self.tearDown()

        try:
            self.driver.find_element_by_xpath("/html/body/form/div[6]/div/div[1]/div/div[8]/img")
            self.driver.save_screenshot(screenshot_path + "\\Step2_help.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find Help menu item")
            self.driver.save_screenshot(screenshot_path + "\\Step2_help.png")
            self.tearDown()

        try:
            sign_out = self.driver.find_element_by_xpath("/html/body/form/div[6]/div/div[2]/div[3]/div[1]/a")
            self.driver.save_screenshot(screenshot_path + "\\Step2_sign_out.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find Sign Out menu item")
            self.driver.save_screenshot(screenshot_path + "\\Step2_sign_out.png")
            self.tearDown()

        try:
            my_account = self.driver.find_element_by_xpath("/html/body/form/div[6]/div/div[2]/div[3]/div[3]/a")
            self.driver.save_screenshot(screenshot_path + "\\Step2_my_account.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find My Account menu item")
            self.driver.save_screenshot(screenshot_path + "\\Step2_my_account.png")
            self.tearDown()

        try:
            self.driver.find_element_by_xpath("/html/body/form/div[6]/div/div[2]/div[3]/div[5]/a")
            self.driver.save_screenshot(screenshot_path + "\\Step2_help.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find Help menu item")
            self.driver.save_screenshot(screenshot_path + "\\Step2_help.png")
            self.tearDown()

    # expected results3:
    # Log in page displays
    def test_Step3_sign_out(self):
        self.login()
        self.sign_out()

        try:
            self.driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr/td/div/div[4]/div[1]")
            self.driver.save_screenshot(screenshot_path + "\\Step3_SignOut.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find Sign Out control")
            self.driver.save_screenshot(screenshot_path + "\\Step3_SignOut.png")
            self.tearDown()

    # expected result4:
    # Please enter your username.
    # Please enter your password.
    def test_Step4_click_login(self):
        self.login()
        self.sign_out()
        self.click_login()
        
        try:
            self.driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr/td/div/div[6]")
            self.driver.save_screenshot(screenshot_path + "\\Step4_ClickLogin.png")
        except NoSuchElementException:
            self.assertTrue(False, "Can not find login/password text")
            self.driver.save_screenshot(screenshot_path + "\\Step4_ClickLogin.png")
            self.tearDown()

    # expected result5:
    # Your username or password is invalid. Please try again.
    def test_Step5_input_invalid_username_password(self):
        self.login()
        self.sign_out()
        self.click_login()
        self.input_invalid_username_password()

        try:
            self.driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr/td/div/div[6]")
            self.driver.save_screenshot(screenshot_path + "\\Step5_InvalidUsernamePassword.png")
        except NoSuchElementException:
            self.assertTrue(False, "Invalid Username or Password text not displayed")
            self.driver.save_screenshot(screenshot_path + "\\Step5_InvalidUsernamePassword.png")
            self.tearDown()

    # expected result6:
    # Your username or password is invalid. Please try again.
    def test_Step6_input_valid_username_invalid_password(self):
        self.input_valid_username_invalid_password()
        self.click_login()

        try:
            self.driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr/td/div/div[6]")
            self.driver.save_screenshot(screenshot_path + "\\Step6_ValidUsernameInvalidPassword.png")
        except NoSuchElementException:
            self.assertTrue(False, "Invalid Username or Password text not displayed")
            self.driver.save_screenshot(screenshot_path + "\\Step6_ValidUsernameInvalidPassword.png")
            self.tearDown()

    # expected results7:
    # https://uat-bioinventory.biostorage.com/SendUsername.aspx
    # page displays
    def test_Step7_click_forget_your_username_link(self):
        self.click_forget_your_username_link()

        try:
            self.driver.find_element_by_xpath("/html/body/form/div[8]/div/h2")
            self.driver.save_screenshot(screenshot_path + "\\Step7_Forget_Username_Link.png")
        except NoSuchElementException:
            self.assertTrue(False, "Forget your user name? page not displayed.")
            self.driver.save_screenshot(screenshot_path + "\\Step7_Forget_Username_Link.png")
            self.tearDown()

    # expected results8:
    # https://uat-bioinventory.biostorage.com/Profile/Account/ForgotPassword
    # page displays
    def test_Step8_click_back_on_browser(self):
        self.click_back_on_browser()

        try:
            self.driver.find_element_by_xpath("/html/body/form/div[3]/img")
            self.driver.save_screenshot(screenshot_path + "\\Step8_Click_Back_On_Browser.png")
        except NoSuchElementException:
            self.assertTrue(False, "Failed to click back on browser")
            self.driver.save_screenshot(screenshot_path + "\\Step8_Click_Back_On_Browser.png")
            self.tearDown()

    # expected results9:
    # uat-bioinventory.biostorage.com/profile/account/phone page displays
    # Site Navigation menu: BioInventory, Sample Info, Transport, Reports, Disposal, Lab Services, BioInsight, Help
    # User links: Sign Out, My Account, Help
    def test_Step9_click_forgot_your_password(self):
        self.click_forgot_your_password()

        try:
            self.driver.find_element_by_xpath("/html/body/div[3]/div/h2")
            self.driver.save_screenshot(screenshot_path + "\\Step9_Forgot_Password.png")
        except NoSuchElementException:
            self.assertTrue(False, "Forgot your password? page not displayed")
            self.driver.save_screenshot(screenshot_path + "\\Step9_Forgot_Password.png")
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
