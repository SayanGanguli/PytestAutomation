import pytest
from Automation_Helper.BasePage import BaseEngine
from B2B_Pages.HomePage import HomePage
from B2B_Pages.LoginPage import LoginFeature


class TestSearchFeature(BaseEngine):

    @pytest.mark.order("fifth")
    @pytest.mark.search
    def testSearch(self):
        login = LoginFeature(self.driver)
        login.launchB2B_Page()
        login.loginToApplicaton()

        home = HomePage(self.driver)
        home.openSearchBar()
        home.searchItemWithSuggestion("Printers")
        home.selectFromSuggestion(1)
        home.verifySearchedItem()

        home.openSearchBar()
        home.searchItemWithSuggestion("Image")
        home.selectFromSuggestion(1)
        home.verifySearchedItem()

        home.openSearchBar()
        home.searchItemWithoutSuggestion("Camera")
        home.verifySearchedItem()
