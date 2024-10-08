import pytest
from Automation_Helper.BasePage import BaseEngine
from B2B_Pages.HomePage import HomePage
from B2B_Pages.LoginPage import LoginFeature
from B2B_Pages.ProductPage import Product
from B2B_Pages.EmailPage import EmailValidation


class TestOrderPlacementValidations(BaseEngine):

    @pytest.mark.ord
    @pytest.mark.order("ninth")
    def testOrderPlacement_SingleShipping(self):
        login = LoginFeature(self.driver)
        login.launchB2B_Page()
        login.loginToApplicaton()

        home = HomePage(self.driver)
        home.navigateToProductList()
        home.selectProductCategory("Colour printers")

        prod = Product(self.driver)
        prod.selectSingleProduct("Canon imageRUNNER ADVANCE C478iF")
        prod.configureYourDevice()
        prod.addToCart()
        prod.goToCartDetails()
        prod.processToCheckout()
        prod.enterShippingAddress()
        prod.proceedToPayment()
        prod.selectTCCheckbox()
        prod.submitOrderRequest()
        prod.verifyOrderConfirmation()

    @pytest.mark.ord
    @pytest.mark.order("tenth")
    def testPrintPurchaseOrder_Store(self):
        prod = Product(self.driver)
        order_number = prod.fetchOrderNumber()
        purchase_number = prod.fetchPurchaseNumber()

        home = HomePage(self.driver)
        home.goToAccountProfile()
        home.clickAccountOptions("Order History")
        home.openLatestOrderDetails()
        home.clickPrintPurchaseOrder()
        prod.validateOrderDetails(order_number, purchase_number)

    @pytest.mark.ord
    @pytest.mark.order("eleventh")
    def testValidateEmail(self):
        em = EmailValidation(self.driver)
        em.launchMailPage()
        em.enterEMail()
        em.clickArrowButton()
        em.checkMailContent()
