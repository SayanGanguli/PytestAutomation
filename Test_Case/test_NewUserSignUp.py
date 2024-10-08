from Automation_Helper.BasePage import BaseEngine
import pytest
from B2B_Pages.RegistrationPage import Registration
from Resource_Data import TestData
from B2B_Pages.EmailPage import EmailValidation
from B2B_Pages.LoginPage import LoginFeature


class TestNewUserRegistration(BaseEngine):
    mail = TestData.new_mail

    @pytest.mark.order("second")
    @pytest.mark.signup
    def testSignUpFlow(self):
        log = LoginFeature(self.driver)
        log.launchB2B_Page()
        reg = Registration(self.driver)
        reg.registerNewUser()
        reg.selectCountry("Norway")
        reg.selectLanguage("English")
        reg.clickStepButton("NEXT STEP")
        reg.enterNewUserEmail(self.mail)
        tc_boxes = ["Email", "Phone", "Post"]
        for i in tc_boxes:
            reg.clickCheckBoxes(i)
        reg.clickStepButton("NEXT STEP")
        reg.enterPrimaryContactDetails()
        reg.clickStepButton("NEXT STEP")
        reg.enterBusinessDetails()
        reg.clickStepButton("NEXT STEP")
        reg.expandSummaryPage("Business Details")
        reg.clickStepButton("Submit")

    @pytest.mark.order("third")
    @pytest.mark.signup
    def testVerifyConfirmationMail(self):
        em = EmailValidation(self.driver)
        em.launchMailPage()
        em.enterEmailToSearch(self.mail)
        em.refreshTheInbox()
        em.goToMailBody()
        em.verifyAccountCreationMail()
        em.clickToVerifyAccount()
