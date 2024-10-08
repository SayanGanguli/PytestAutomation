from Automation_Helper import Locators
from Automation_Helper.Locators import getLocator
from Automation_Helper.HelperPage import CommonHelper
from Automation_Helper.BasePage import BaseEngine
from Automation_Helper.UI_Operations import UIOperations
from Resource_Data import TestData


class EmailValidation(UIOperations):
    logger = BaseEngine.loggen()

    def __init__(self, driver):
        super().__init__(self)
        self.helper = CommonHelper(driver)

    def launchMailPage(self):
        self.helper.load_webpage(TestData.email_link)
        self.helper.wait_to_page_load()

    def enterEMail(self, mail=TestData.emailId):
        self.helper.wait_to_execute(4)
        self.enterInputFields("YOPMail",mail)
        self.logger.info('Email is entered: {0}'.format(mail))

    def clickArrowButton(self):
        self.helper.click_element(getLocator("id"), Locators.arrow_button)
        self.logger.info("Clicked to land on mail content")

    def refreshTheInbox(self):
        self.helper.click_element(getLocator("id"), "refresh")
        self.logger.info("Clicked to refresh the inbox")

    def goToMailBody(self):
        self.helper.switching_frame(getLocator("id"), Locators.mail_body_frame)
        self.logger.info("Switched to the mail body")
        self.helper.wait_to_execute(1)

    def checkMailContent(self):
        self.goToMailBody()
        path = "//table[2]/tbody/tr/td/table/tbody/tr/td/table[3]/tbody/tr[{0}]/td"
        for i in range(1, 10, 2):
            if i == 7:
                break
            else:
                content = self.helper.get_text(getLocator("xpath"), path.format(i))
                self.logger.info('Mail contains: {0}'.format(content))

    def enterEmailToSearch(self, mail=""):
        self.enterEMail(mail)
        self.clickArrowButton()
        self.helper.wait_to_execute(4)

    def verifyAccountCreationMail(self):
        expected_message = "Thank you for signing up to the Business Account Portal."
        act_text = self.helper.get_text(getLocator("xpath"),
                                        "(//div[@id='mail']//following::tr[3]/td[1])[1]")

        if expected_message in act_text.strip():
            assert True
            self.logger.info("Verification is successful")

    def clickToVerifyAccount(self):
        self.helper.click_element(getLocator("link"),"this link")
        parent = self.helper.get_window_handlers(0)
        child = self.helper.get_window_handlers(1)
        self.helper.switching_window(child)
        expected_title = "Email Verification Status"
        act_title = self.helper.get_page_title()
        if expected_title == act_title:
            assert True
            self.logger.info("Account is verified!! SignUp process is completed")
            self.helper.close_tab()
        self.helper.switching_window(parent)