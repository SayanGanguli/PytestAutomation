from Automation_Helper import Locators
from Automation_Helper.Locators import getLocator
from Automation_Helper.HelperPage import CommonHelper
from random import randint
from Automation_Helper.BasePage import BaseEngine
from Automation_Helper.UI_Operations import UIOperations


class Product(UIOperations):
    logger = BaseEngine.loggen()

    def __init__(self, driver):
        super().__init__(self)
        self.helper = CommonHelper(driver)

    def selectSingleProduct(self, product):
        item = "//span[text()='{0}']".format(product)
        self.helper.wait_for_element_visible(getLocator("xpath"), item,20)
        self.helper.click_element(getLocator("xpath"), item)
        self.logger.info("Product {0} is selected".format(product))
        self.helper.wait_to_execute(3)

    def configureYourDevice(self):
        self.helper.wait_to_execute(5)
        self.helper.click_to_execute(getLocator("xpath"), Locators.device_configure_button)
        self.logger.info("Device is configured")
        self.helper.wait_to_execute(2)

    def addToCart(self):
        self.helper.click_element(getLocator("xpath"), Locators.add_to_cart)
        self.logger.info("Product is added to the cart")
        self.helper.wait_to_execute(2)

    def goToCartDetails(self):
        self.helper.wait_to_execute(4)
        self.helper.click_element(getLocator("xpath"), Locators.view_cart)
        self.logger.info("Product details in Cart")
        self.helper.wait_for_element_visible(getLocator("xpath"), Locators.order_desktop_view)
        self.helper.click_element(getLocator("xpath"), Locators.order_desktop_view)

    def processToCheckout(self):
        self.helper.click_element(getLocator("xpath"), Locators.checkout_button)
        self.logger.info("Product is processed for checkout")
        self.helper.wait_to_execute(2)

    def clickAddressDropDown(self):
        self.helper.click_element(getLocator("xpath"), Locators.address_ddn)
        self.logger.info("Address dropdown is displaying")
        self.helper.wait_to_execute(4)

    def selectAddress(self):
        self.helper.click_element(getLocator("xpath"), Locators.address1)
        self.logger.info("First Address is selected from dropdown")

    def enterShippingAddress(self):
        self.clickAddressDropDown()
        self.selectAddress()

    def submitOrderRequest(self):
        self.helper.waitForElementClickable(getLocator("xpath"), Locators.order_request)
        self.helper.click_element(getLocator("xpath"), Locators.order_request)
        self.logger.info("Order request is submitted")

    def proceedToPayment(self):
        self.helper.wait_to_execute(3)
        self.submitOrderRequest()

    def enterPurchaseNumber(self):
        purch_num = randint(10, 99999)
        self.helper.enter_text(getLocator("xpath"), Locators.purchase_number, purch_num)
        self.helper.wait_to_execute(1)
        self.logger.info('Purchased Number is {0}'.format(purch_num))

    def clickCheckBox(self):
        self.helper.click_to_execute(getLocator("xpath"), Locators.tc_checkbox)

    def selectTCCheckbox(self):
        self.enterPurchaseNumber()
        self.clickCheckBox()
        self.logger.info("T&C Checkbox is selected")

    def orderConfirmation(self):
        message = self.helper.get_text(getLocator("xpath"), Locators.order_confirmation)
        self.logger.info('Order confirmation message is {0}'.format(message))
        return message

    def fetchOrderNumber(self):
        msg = self.orderConfirmation()
        exp_order_number = ""
        for i in msg:
            if i == "U":
                exp_order_number = exp_order_number + i
            if i.isdigit():
                exp_order_number = exp_order_number + i

        self.logger.info("Order Number is: {0}".format(exp_order_number))
        return exp_order_number

    def fetchPurchaseNumber(self):
        p_num = self.helper.get_text(getLocator("xpath"), Locators.fetched_invoice_no)
        return p_num

    def verifyOrderConfirmation(self):
        actual_text = self.orderConfirmation()
        self.logger.info("Order confirmation message: " + actual_text)
        if "U" in actual_text:
            assert True
            self.logger.info("Verification is successful")
        else:
            self.logger.info("Verification is not successful")
            assert False
        self.helper.wait_to_execute(5)

    def addToCompare(self):
        self.helper.click_element(getLocator("css"), Locators.add_compare_button)
        self.logger.info("Product is added to compare")

    def removeConfiguration(self):
        self.helper.click_element(getLocator("css"), Locators.remove_configuration_button)
        self.logger.info("Configuration is removed")

    def clickPurchaseOptions(self, act):
        icon = ""
        if act.lower() == "show":
            icon = "arrow-down"
        elif act.lower() == "hide":
            icon = "arrow-up"
        self.helper.click_element(getLocator("xpath"), "//i[contains(@class,'{0}')]".format(icon))

    def closeConfiguratorModal(self):
        self.helper.click_element(getLocator("xpath"), Locators.configurator_modal_close_icon)

    def selectPurchaseOption(self, opt):
        index = 0
        if opt == "Lease":
            index = 1
        elif opt == "Direct":
            index = 2
        self.helper.click_element(getLocator("xpath"),
                                  "//div[@class='bundle-selector--purchasing-option-wrapper']/div[{0}]".format(index))

    def compareMultipleProducts(self):
        self.helper.click_element(getLocator("xpath"), Locators.compare_products_button)
        self.logger.info("Products are now compared")
        self.helper.wait_to_page_load(5)

    def removeAllProductsFromComparison(self):
        self.helper.click_element(getLocator("xpath"), Locators.allcomparison_remove_button)
        self.logger.info("Products are now removed from comparison")

    def removeSingleProductFromComparison(self, prod_order=2):
        path = "(//span[@class='removeBtnText'])[{0}]/font/font".format(prod_order)
        button = self.helper.get_text(getLocator("xpath"), path)
        if button != "Remove all":
            self.helper.click_element(getLocator("xpath"), path)
            self.logger.info("Number {0} product is removed".format(prod_order))
        else:
            self.removeAllProductsFromComparison()

    def comparePrices(self):
        self.helper.click_element(getLocator("xpath"), Locators.compare_price_button)

    def validateOrderDetails(self, exp_order_num, exp_purchase_num):
        details = []
        order_details = self.helper.get_elements(getLocator("xpath"), Locators.order_details_info)
        for order in order_details:
            details.append(order.text)
        self.logger.info("Order Details: {0} ".format(details))
        act_order_no = self.helper.get_text(getLocator("xpath"), Locators.fetched_order_no)
        act_name = details[0]
        act_email = details[2]
        act_purchase_num = details[3]
        act_framework = details[4]

        assert act_order_no == exp_order_num
        assert act_name == "NO Sandeep"
        assert act_email == "sandeep_no@yopmail.com"
        assert act_framework == "NO Framework"
        assert act_purchase_num == exp_purchase_num
        self.logger.info("Verification of order details is successful")