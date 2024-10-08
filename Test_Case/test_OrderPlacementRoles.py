import pytest
from Automation_Helper.BasePage import BaseEngine
from B2B_Pages.HomePage import HomePage
from B2B_Pages.LoginPage import LoginFeature
from B2B_Pages.ProductPage import Product


class TestOrderPlacementWithVariousRoles(BaseEngine):

    @pytest.mark.critical
    @pytest.mark.order("sixteenth")
    def testOrderPlacementWithVariousRoles(self):
        login = LoginFeature(self.driver)
        login.launchB2B_Page()
        login.loginToApplicaton()

        home = HomePage(self.driver)
        home.navigateToProductList()
        home.selectProductCategory("Colour printers")

        prod = Product(self.driver)
        prod.selectSingleProduct("Canon imageRUNNER ADVANCE DX C257iF")
        prod.configureYourDevice()
        prod.addToCart()
        prod.goToCartDetails()
        prod.processToCheckout()
        prod.enterShippingAddress()
        prod.submitOrderRequest()
        prod.selectTCCheckbox()
        prod.submitOrderRequest()
        prod.verifyOrderConfirmation()
