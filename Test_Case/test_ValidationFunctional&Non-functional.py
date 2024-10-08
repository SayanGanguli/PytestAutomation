from Automation_Helper.BasePage import BaseEngine
from B2B_Pages.HomePage import HomePage
from B2B_Pages.LoginPage import LoginFeature
import pytest


class TestValidateOperations(BaseEngine):

    @pytest.mark.order("eighth")
    @pytest.mark.func
    def testValidateFunctional(self):
        login = LoginFeature(self.driver)
        login.launchB2B_Page()
        login.loginToApplicaton()

        home = HomePage(self.driver)
        primary_footer = ["Contact Us", "Delivery information", "Proforma invoice", "FAQ"]
        corporate_footer = ["Terms and conditions", "Privacy Guidlines", "Availability"]
        for i in primary_footer:
            home.clickToPrimaryFooter(i)

        for j in corporate_footer:
            home.clickToCorporateFooter(j)

        home.clickCookieSettingFooter()
