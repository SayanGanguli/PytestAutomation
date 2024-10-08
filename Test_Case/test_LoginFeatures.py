import pytest
from Automation_Helper.BasePage import BaseEngine
from B2B_Pages.LoginPage import LoginFeature
from B2B_Pages.HomePage import HomePage


class TestLoginFlow(BaseEngine):

    @pytest.mark.order("first")
    @pytest.mark.sign
    def testExistUser_SignInFlow(self):
        login = LoginFeature(self.driver)
        home = HomePage(self.driver)
        login.launchB2B_Page()
        login.loginToApplicaton()
        home.logoutFromApplication()