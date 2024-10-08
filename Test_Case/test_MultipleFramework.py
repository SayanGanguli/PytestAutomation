import pytest
from Automation_Helper.BasePage import BaseEngine
from B2B_Pages.OCCPage import OCCFeatures


class TestMultipleFramework_VariousRoles(BaseEngine):

    @pytest.mark.frame
    @pytest.mark.order("fourteenth")
    def testVariousRoles(self):
        occ = OCCFeatures(self.driver)
        occ.launchAdminPage()
        occ.loginToApplicaton()
        occ.waitForAdminDashboardPage()
        occ.navigateLeftPanelMenu("Accounts")
        occ.navigateAccountsSubMenu("Contacts List")
        occ.filterAnAccount()
        occ.clickFilteredAccount()
        occ.navigateAccountsSubMenu("Account Memberships")
        occ.verifyRoleSelection()

    @pytest.mark.frame
    @pytest.mark.order("fifteenth")
    def testMultipleFramework(self):
        occ = OCCFeatures(self.driver)
        occ.navigateLeftPanelMenu("Catalog")
        occ.selectCatalog("B2B Catalog")
        occ.filterWithCatalog("Canon imageRUNNER ADVANCE C3835i")
        occ.selectFilteredCatalog()
        occ.navigateMenuOfModal("Price Groups")
        occ.filterPriceGroup("NO B2B")
        occ.editFilteredPriceGroup()
        occ.fetchRange_PriceDetails()
