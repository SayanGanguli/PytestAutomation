import pytest
from Automation_Helper.BasePage import BaseEngine
from B2B_Pages.HomePage import HomePage
from B2B_Pages.LoginPage import LoginFeature
from B2B_Pages.ProductPage import Product


class TestConfiguratorValidations(BaseEngine):

    @pytest.mark.config
    @pytest.mark.order("thirteenth")
    def testValidation_Configurator(self):
        login = LoginFeature(self.driver)
        login.launchB2B_Page()
        login.loginToApplicaton()

        home = HomePage(self.driver)
        home.navigateToProductList()
        home.selectProductCategory("Colour printers")

        prod = Product(self.driver)
        prod.selectSingleProduct("Canon imageRUNNER ADVANCE C3835i")
        prod.configureYourDevice()
        prod.addToCompare()
        prod.clickPurchaseOptions("Show")
        prod.closeConfiguratorModal()
        prod.backToPage()
        prod.selectSingleProduct("Canon imageRUNNER ADVANCE DX C257iF")
        prod.configureYourDevice()
        prod.addToCompare()
        prod.compareMultipleProducts()
