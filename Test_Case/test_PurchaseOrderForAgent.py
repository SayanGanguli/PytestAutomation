from B2B_Pages.OCCPage import OCCFeatures
from Automation_Helper.BasePage import BaseEngine
import pytest


class TestPrintPurchaseOrderForAgent(BaseEngine):

    @pytest.mark.order("Twelfth")
    def testPrintPurchaseOrder_Agent(self):
        occ = OCCFeatures(self.driver)
        occ.launchAgentPage()
        occ.loginToApplicaton()
        occ.waitForAgentDashboardPage()
        occ.clickAgentOrderButton()
        occ.searchOrderNumber("U390505")
        occ.clickSearchButton()
        occ.fetchOrderDetails()
        occ.validateOrderDetails()
