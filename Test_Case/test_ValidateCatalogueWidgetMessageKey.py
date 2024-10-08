from Automation_Helper.BasePage import BaseEngine
import pytest
from B2B_Pages.HomePage import HomePage
from B2B_Pages.LoginPage import LoginFeature


class TestValidationOfSectors(BaseEngine):

    @pytest.mark.order("seventh")
    def testValidateCatalogue(self):
        login = LoginFeature(self.driver)
        login.launchB2B_Page()
        login.loginToApplicaton()
        home = HomePage(self.driver)
        home.logoutFromApplication()
