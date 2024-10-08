import pytest
from Automation_Helper.BasePage import BaseEngine
from B2B_Pages.EmailPage import EmailValidation
from B2B_Pages.LoginPage import LoginFeature
from Resource_Data import TestData


class TestResetPassword(BaseEngine):

    @pytest.mark.res
    @pytest.mark.order("fourth")
    def testForgotPassword(self):
        login = LoginFeature(self.driver)
        login.launchB2B_Page()
        login.clickResetPasswordButton()
        login.enterMailToReset(TestData.dummy_mail)
        login.clickSendMailButton()

        # em = EmailValidation(self.driver)
        # em.launchMailPage()
        # em.enterEmailToSearch()
        # em.goToMailBody()
