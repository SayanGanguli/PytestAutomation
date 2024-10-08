from Automation_Helper.HelperPage import CommonHelper
from Automation_Helper import Locators
from Automation_Helper.Locators import getLocator
from Automation_Helper.BasePage import BaseEngine
from Automation_Helper.UI_Operations import UIOperations
from Resource_Data import TestData


class OCCFeatures(UIOperations):
    logger = BaseEngine.loggen()

    def __init__(self, driver):
        super().__init__(self)
        self.helper = CommonHelper(driver)

    def launchAdminPage(self):
        self.helper.load_webpage(TestData.admin_url)
        self.helper.wait_to_page_load(20)

    def launchAgentPage(self):
        self.helper.load_webpage(TestData.agent_url)
        self.helper.wait_to_page_load(20)

    def enterCredentials(self, field, value):
        txt = ""
        if field == "username":
            txt = "User name or email"
        elif field == "password":
            txt = "Password"
        else:
            pass
        self.helper.enter_text(getLocator("xpath"), "//input[@placeholder='{0}']".format(txt), value)

    def clickSignInButton(self):
        self.helper.click_element(getLocator("xpath"), Locators.occ_signin_button)
        self.helper.wait_to_page_load()

    def waitForAgentDashboardPage(self):
        self.helper.wait_for_element_visible(getLocator("xpath"), Locators.occ_dashboard_page)

    def waitForAdminDashboardPage(self):
        self.helper.wait_for_element_visible(getLocator("id"), "[[titleId]]")

    def loginToApplicaton(self):
        self.enterCredentials("username", TestData.occ_uname)
        self.logger.info("Entered The Valid UserName")
        self.enterCredentials("password", TestData.occ_pwd)
        self.logger.info("Entered The valid Password")
        self.clickSignInButton()
        self.logger.info("Clicked Sign In Button")

    def clickAgentOrderButton(self):
        self.helper.wait_for_element_visible(getLocator("xpath"), Locators.agent_ordersearch_menu)
        self.helper.click_element(getLocator("xpath"), Locators.agent_ordersearch_menu)

    def searchOrderNumber(self, value):
        self.helper.enter_text(getLocator("xpath"), Locators.orderid_field, value)
        self.helper.wait_to_execute(5)

    def clickSearchButton(self):
        self.helper.wait_for_element_visible(getLocator("id"), Locators.order_search_button)
        self.helper.click_element(getLocator("id"), Locators.order_search_button)
        self.helper.wait_to_execute(5)

    def clickResetButton(self):
        self.helper.click_element(getLocator("id"), Locators.order_reset_button)

    def fetchOrderDetails(self, key=""):
        details = {}
        columnHeads = []
        results = []
        objects = self.helper.get_elements(getLocator("xpath"), Locators.searchtable_columnheads)
        for col in objects:
            columnHeads.append(col.text)

        objects = self.helper.get_elements(getLocator("xpath"), Locators.searchtable_rowvalues)
        for res in objects:
            results.append(res.text)
        for i in range(len(columnHeads)):
            details.update({columnHeads[i]: results[i]})
        self.logger.info("Order Details: {0} ".format(details))
        return details.get(key)

    def validateOrderDetails(self):
        order_no = self.fetchOrderDetails("Order Number")
        act_account = self.fetchOrderDetails("Account")
        act_fname = self.fetchOrderDetails("First Name")
        act_lname = self.fetchOrderDetails("Last Name")
        act_email = self.fetchOrderDetails("Email")
        act_total = self.fetchOrderDetails("Order Total")
        self.helper.click_element(getLocator("xpath"), "//a[text()='{0}']".format(order_no))
        self.helper.wait_for_element_visible(getLocator("xpath"), Locators.print_confirmation_button)

        exp_account = self.helper.get_text(getLocator("id"), Locators.order_account_name)
        exp_lname = self.helper.get_text(getLocator("id"), Locators.order_user_lastname)
        exp_fname = self.helper.get_text(getLocator("id"), Locators.order_user_firstname)
        exp_email = self.helper.get_text(getLocator("id"), Locators.order_user_email)
        exp_total = self.helper.get_text(getLocator("id"), Locators.order_totalValue)

        assert exp_account == act_account
        assert exp_lname == act_lname
        assert exp_fname == act_fname
        assert exp_email == act_email
        assert exp_total == act_total
        self.logger.info("Verification of order details is successful")

    def navigateLeftPanelMenu(self, menu):
        self.helper.click_element(getLocator("xpath"), "//span[@title='{0}']".format(menu))
        self.logger.info("Navigating to the menu {0}".format(menu))
        self.helper.wait_to_execute(7)

    def navigateAccountsSubMenu(self, sub_menu):
        self.helper.click_element(getLocator("xpath"), "//span[text()='{0}']".format(sub_menu))
        self.logger.info("Navigating to the submenu {0}".format(sub_menu))
        self.helper.wait_to_page_load()

    def selectCatalog(self, catalog_name):
        self.helper.wait_to_execute(4)
        self.helper.click_element(getLocator("id"), Locators.catalog_ddn_button)
        self.helper.wait_for_element_visible(getLocator("xpath"), "//span[@title='{0}']".format(catalog_name))
        self.helper.click_element(getLocator("xpath"), "//span[@title='{0}']".format(catalog_name))
        self.logger.info("Catalog {0} is selected".format(catalog_name))

    def filterAnAccount(self):
        self.helper.enter_text(getLocator("xpath"), Locators.filter_account_field, TestData.account_name)
        self.logger.info("Entered the account name: {0}".format(TestData.occ_uname))
        self.helper.wait_to_execute(2)

    def clickFilteredAccount(self):
        self.helper.click_element(getLocator("xpath"), Locators.filtered_account)
        self.logger.info("Clicked the filtered account")
        self.helper.wait_to_execute(7)

    def selectAccount(self):
        self.navigateAccountsSubMenu("No Company")

    def verifyRoleSelection(self):
        role = self.helper.get_text(getLocator("xpath"), Locators.role_No_Company)
        if role == "Account Address Manager, Administrator, Approver, Buyer, Profile Address Manager":
            assert True
            self.logger.info("Role is selected")

    def filterWithCatalog(self, prod):
        self.helper.wait_to_execute(2)
        self.helper.enter_text(getLocator("xpath"), Locators.filter_catalog_field, prod)
        self.logger.info("Filtered the catalog: {0}".format(prod))
        self.helper.wait_to_execute(5)
        self.helper.click_element(getLocator("xpath"), "//div[text()='{0}']".format(prod))

    def selectFilteredCatalog(self):
        self.logger.info("The Catalog is selected")
        self.helper.wait_to_execute(2)
        self.helper.wait_for_element_visible(getLocator("xpath"), Locators.edit_catalog_icon)
        self.helper.click_element(getLocator("xpath"), Locators.edit_catalog_icon)

    def navigateMenuOfModal(self, menu):
        self.helper.wait_for_element_visible(getLocator("id"), Locators.product_modal_menu)
        self.logger.info("Modal of product details is displayed")
        self.helper.click_element(getLocator("xpath"), "//a[text() = '{0}']".format(menu))
        self.logger.info("Navigated to the menu: {0}".format(menu))
        self.helper.wait_to_execute(2)

    def filterPriceGroup(self, price_group):
        self.helper.enter_text(getLocator("xpath"), Locators.filter_pricegroup_menu, price_group)
        self.helper.wait_to_execute(2)
        self.helper.press_space_key()
        self.logger.info("Filtered the price group with {0}".format(price_group))
        self.helper.wait_to_execute(2)

    def editFilteredPriceGroup(self):
        self.helper.click_element(getLocator("xpath"), Locators.edit_pricegroup_icon)
        self.helper.wait_for_element_visible(getLocator("id"), Locators.price_modal_window)
        self.logger.info("Editing prices modal is displaying")

    def fetchRange_PriceDetails(self):
        range_start = self.helper.get_text(getLocator("xpath"), Locators.min_range_slot1)
        range_end = self.helper.get_text(getLocator("xpath"), Locators.max_range_slot1)
        range_start1 = self.helper.get_text(getLocator("xpath"), Locators.min_range_slot2)
        self.logger.info(range_start + " " + range_end + " " + range_start1)

    def clickAccountIcon(self):
        self.helper.wait_to_execute(2)
        self.helper.waitForElementClickable(getLocator("xpath"), Locators.account_topmenu_icon)
        self.helper.click_element(getLocator("xpath"), Locators.account_topmenu_icon)
        self.logger.info("Account Icon is clicked")

    def clickLogout(self):
        self.clickAccountIcon()
        self.helper.waitForElementClickable(getLocator("xpath"), Locators.occ_logout_Button)
        self.helper.click_element(getLocator("xpath"), Locators.occ_logout_Button)
        self.logger.info("Logout from the application")
        self.helper.wait_to_execute(2)
