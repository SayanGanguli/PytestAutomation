from Automation_Helper.BasePage import BaseEngine
import pytest
from B2B_Pages.HomePage import HomePage
from B2B_Pages.LoginPage import LoginFeature
from Resource_Data import TestData


class TestContentsPages(BaseEngine):

    @pytest.mark.order("sixth")
    @pytest.mark.content
    def testContents(self):
        login = LoginFeature(self.driver)
        login.launchB2B_Page()
        login.loginToApplicaton()

        home = HomePage(self.driver)

        home.verifyFooterData()
        home.clickHeaderLink("Help")
        home.clickHeaderLink("Shop")
        home.goToAccountProfile()
        home.clickAccountOptions("My Account")
        home.validateMyAccountPage()
        home.clickEditAccount()

        home.goToContentMenu("Address")
        home.clickAddNewDeliveryAddressButton()
        field = ["Address1", "Address2", "City", "Phone Number", "Post"]
        value = [TestData.generateRandomString(), TestData.generateRandomString(), "Hamburger", "9876543201",
                 TestData.generateRandomNumber()]
        for i in range(len(field)):
            home.addNewDeliveryAddress(field[i], value[i])
        home.selectState()
        home.save_cancelAddress("Save")

        home.clickAddressType("Billing")
        home.selectDefaultAddress(2)
        home.goToAccountProfile()
        home.clickAccountOptions("Order History")
        home.sortOrderByPeriod("All")
        home.sortOrderByStatus("Rejected")
