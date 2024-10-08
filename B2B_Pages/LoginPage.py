from Automation_Helper.BasePage import BaseEngine
from Automation_Helper.HelperPage import CommonHelper
from Automation_Helper import Locators
from Automation_Helper.Locators import getLocator
from Automation_Helper.UI_Operations import UIOperations
from Resource_Data import TestData


class LoginFeature(UIOperations):
    logger = BaseEngine.loggen()

    def __init__(self, driver):
        super().__init__(self)
        self.helper = CommonHelper(driver)

    def launchB2B_Page(self):
        self.helper.load_webpage(TestData.url)
        self.helper.wait_to_page_load(20)
        self.clickToLogin_RegisterButton()

    def enableTheCookies(self):
        try:
            self.helper.wait_for_element_visible(getLocator("id"), Locators.accepting_cookies)
            self.helper.click_element(getLocator("id"), Locators.accepting_cookies)
            self.logger.info("Accepted The Cookies")
        except Exception:
            print("No Popup")

    def clickToLogin_RegisterButton(self):
        self.enableTheCookies()
        self.helper.wait_for_element_visible(getLocator("xpath"), Locators.login_register_button)
        self.helper.click_element(getLocator("xpath"), Locators.login_register_button)
        self.logger.info("Clicked The Login/Register Button")

    def clickSignIn(self):
        self.helper.click_element(getLocator("xpath"), Locators.login_Button)
        self.helper.waitForMainPage(getLocator("xpath"), Locators.product_page)
        self.enableTheCookies()

    def loginToApplicaton(self):
        self.enterInputFields("UserName", TestData.uname)
        self.logger.info("Entered The Valid UserName")
        self.enterInputFields("Password", TestData.pwd)
        self.logger.info("Entered The valid Password")
        self.clickSignIn()
        self.logger.info("Clicked Sign In Button")

    def clickResetPasswordButton(self):
        self.helper.click_element(getLocator("id"), "onCustomersForgotPassword")
        self.logger.info("Reset Password link is clicked")

    def enterMailToReset(self, mail):
        self.enterInputFields("UserName", mail)
        self.logger.info("Entered the username to update password")

    def clickSendMailButton(self):
        self.clickButton_Text("Send email")
        self.logger.info("Clicked send mail button")

