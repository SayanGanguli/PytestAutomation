from Automation_Helper import Locators
from Automation_Helper.Locators import getLocator
from Automation_Helper.HelperPage import CommonHelper
from Automation_Helper.BasePage import BaseEngine
from Automation_Helper.UI_Operations import UIOperations


class HomePage(UIOperations):
    logger = BaseEngine.loggen()

    def __init__(self, driver):
        super().__init__(self)
        self.helper = CommonHelper(driver)

    def clickHeaderLink(self, header):
        index = 0
        path = "// ul[@class ='header-links']/li[{0}]/a"
        if header.lower() == "shop":
            index = 1
        elif header.lower() == "help":
            index = 2
        self.logger.info("header selected for {0}".format(header))
        self.helper.click_element(getLocator("xpath"), path.format(index))

    def navigateToProductList(self):
        self.helper.wait_for_element_visible(getLocator("xpath"), Locators.navigation_list)
        self.helper.click_element(getLocator("xpath"), Locators.navigation_list)

    def selectProductCategory(self, product_category):
        index = 0
        if "Colour" in product_category:
            index = 1
        elif "Mono" in product_category:
            index = 2
        elif "Place" in product_category:
            index = 3
        elif "Scanners" in product_category:
            index = 4
        else:
            self.logger.info("No product is selected")

        self.logger.info("{0} category is selected".format(index))
        category = "//ul[@class='sub-Nav container']/li[{0}]/a".format(index)
        self.helper.click_element(getLocator("xpath"), category)

    def goToAccountProfile(self):
        self.helper.click_element(getLocator("xpath"), Locators.account_Icon)
        self.logger.info("Account Modal is open")

    def logoutFromApplication(self):
        self.goToAccountProfile()
        self.helper.click_element(getLocator("xpath"), Locators.logout_Button)
        self.helper.wait_for_element_visible(getLocator("xpath"), Locators.login_register_button)
        self.logger.info("Logout from the application")

    def clickAccountOptions(self, menu):
        index = 0
        if menu.lower() == "my account":
            index = 1
        elif menu.lower() == "address book":
            index = 2
        elif menu.lower() == "order history":
            index = 3

        self.logger.info("Menu is selected: {0}".format(menu))
        path = "//ul[@class='dropdown-profile__list']/li[{0}]/a".format(index)
        self.helper.wait_for_element_visible(getLocator("xpath"), path)
        self.helper.click_element(getLocator("xpath"), path)
        self.helper.wait_to_page_load()
        self.closeMyAccountWindow()

    def closeMyAccountWindow(self):
        self.helper.click_element(getLocator("xpath"), "//span[@class='divider' and text()='>']")

    def openLatestOrderDetails(self):
        self.helper.wait_for_element_visible(getLocator("xpath"), Locators.recent_order_button)
        self.helper.click_element(getLocator("xpath"), Locators.recent_order_button)
        self.helper.wait_for_element_visible(getLocator("css"), Locators.last_order_details)
        self.logger.info("Latest order detail is displaying")

    def clickPrintPurchaseOrder(self):
        self.helper.click_element(getLocator("css"), Locators.purchase_order_link)
        self.logger.info("Clicked print purchase order")

    def openSearchBar(self):
        self.helper.click_element(getLocator("xpath"), "//li/div[@class='Search']/button")
        self.logger.info("Search bar is open")

    def enterInSearchField(self, item):
        self.helper.clear_text_field(getLocator("xpath"), "(//input[@id ='siteSearch'])[2]")
        self.helper.enter_text(getLocator("xpath"), "(//input[@id ='siteSearch'])[2]", item)
        self.logger.info("Finding the item:{0}".format(item))

    def searchItemWithSuggestion(self, item):
        self.enterInSearchField(item)
        self.helper.wait_to_execute(3)
        self.helper.press_space_key()

    def searchItemWithoutSuggestion(self, item):
        self.enterInSearchField(item)
        self.helper.wait_to_execute(2)
        self.helper.press_enter_key()

    def selectFromSuggestion(self, index):
        ele = self.helper.get_elements(getLocator("xpath"), "(//div[@class='Search__TypeaheadResults'])[2]/div/div")
        no_of_suggestion = len(ele)
        self.logger.info("There are {0} no of suggestions".format(no_of_suggestion))
        if no_of_suggestion > index > 0:
            self.helper.click_element(getLocator("xpath"),
                                      "(//div[@class='Search__TypeaheadResults'])[2]/div[{0}]/div".format(index))
        else:
            self.logger.info("Suggestion is not available")

    def verifySearchedItem(self):
        self.helper.wait_for_element_visible(getLocator("xpath"), "//div[contains(@class,'Container search')]/div")
        res = self.helper.get_element_attribute(getLocator("xpath"),
                                                "//div[contains(@class,'Container search')]/div", "class")
        if "original" in res.lower():
            assert "OriginalSearch" in res
            self.logger.info("Item is available")
        else:
            assert "NoResults" in res
            self.logger.info("Item is not available")

        self.helper.refresh_page()

    def verifyFooterData(self):
        path1 = "//div[@class='primary-footer']/descendant::a"
        self.helper.scroll_to_bottom(getLocator("xpath"), path1)
        footer_list = []
        ele = self.helper.get_elements(getLocator("xpath"), path1)
        for i in range(1, len(ele) + 1):
            value = self.helper.get_text(getLocator("xpath"), path1 + "[{0}]".format(i))
            footer_list.append(value)
        self.logger.info(footer_list)

        path2 = "//ul[@class='corporate-footer__nav']/li"
        ele = self.helper.get_elements(getLocator("xpath"), path2)
        for i in range(2, len(ele) + 1):
            if i == len(ele):
                value = self.helper.get_text(getLocator("xpath"), path2 + "[{0}]/descendant::button".format(i))
                footer_list.append(value)
            else:
                value = self.helper.get_text(getLocator("xpath"), path2 + "[{0}]/descendant::a".format(i))
                footer_list.append(value)
        self.logger.info(footer_list)

    def clickEditAccount(self):
        self.helper.click_element(getLocator("xpath"),
                                  "//div[@class='ProfileRecentOrders']/descendant::div[@class='Button-shopAgain__text'][1]")
        self.backToPage()

    def validateMyAccountPage(self):
        row_value = self.helper.get_elements(getLocator("xpath"), "//tbody/tr/td[2]")
        exp_details = ["NO", "Sandeep",
                       "Administrator, Kjøper, Godkjenner, Kontoadressebehandler, Profiladressebehandler",
                       "NO Company", "sandeep_no@yopmail.com"]
        act_details = []

        for i in range(1, len(row_value)):
            value = self.helper.get_text(getLocator("xpath"), "//tbody/tr[{0}]/td[2]".format(i))
            act_details.append(value)
        self.logger.info(act_details)

        for i in range(len(exp_details)):
            assert exp_details[i] == act_details[i]
        self.logger.info("Validation is successful")

    def goToContentMenu(self, menu):
        index = 0
        if menu.lower() == "address":
            index = 2
        elif menu.lower() == "order history":
            index = 3
        elif menu.lower() == "order management":
            index = 4

        self.helper.click_element(getLocator("xpath"),
                                  "//div[@class='myaccount-desktop']/descendant::a[{0}]".format(index))
        self.logger.info("Navigated to {0}".format(menu))
        self.helper.wait_to_page_load()

    def clickAddNewDeliveryAddressButton(self):
        #self.helper.scroll_to_bottom(getLocator("id"), "shippingButton")
        self.helper.wait_to_execute(7)
        self.helper.click_element(getLocator("id"), "shippingButton")
        self.logger.info("Clicked to add new delivery address")

    def addNewDeliveryAddress(self, field, value):
        self.enterInputFields(field, value)

    def selectState(self):
        self.helper.click_element(getLocator("id"), "accountAddressSelect-stateShipping")
        self.helper.click_element(getLocator("id"), "dropdown-state-2")

    def save_cancelAddress(self, button):
        if button.lower() == "save":
            index = 1
        else:
            index = 2
        self.helper.click_to_execute(getLocator("xpath"),
                                     "//div[@class ='AddNewAddressForm__ButtonGroups']/button[{0}]".format(index))

    def clickAddressType(self, type):
        loc = ""
        if type.lower() == "delivery":
            loc = "tab-0"
        elif type.lower() == "billing":
            loc = "tab-1"

        self.helper.wait_to_execute(2)
        self.helper.click_element(getLocator("id"), loc)
        self.logger.info("Clicked tab {0}".format(type))

    def selectDefaultAddress(self, order):
        self.logger.info("Default address is selected "+ str(order))

    def sortOrderByPeriod(self, period):
        self.helper.select_dropdown(getLocator("xpath"),
                                    "//div[@class='SortOptions']/div[1]/div/select", period.lower())
        self.logger.info("Sorted by:{0}".format(period))

    def sortOrderByStatus(self,status):
        self.helper.click_element(getLocator("xpath"),"//div[@class='SortOptions']/div[2]/div/div[1]")
        index = 0
        if status.lower() == "all":
            index = 1
        elif status.lower() == "processed":
            index = 2
        elif status.lower() == "waiting for approval":
            index = 3
        elif status.lower() == "rejected":
            index = 4
        elif status.lower() == "sent in":
            index = 5
        ele = "//div[@class='SortOptions']/descendant::span[{0}]".format(index)
        self.helper.click_element(getLocator("xpath"),ele)
        self.logger.info("Sorted by:{0}".format(status))

    def clickToPrimaryFooter(self,foo):
        index = 0
        if foo.lower() == "contact us":
            index = 1
        elif foo.lower() == "delivery information":
            index = 2
        elif foo.lower() == "proforma invoice":
            index = 3
        elif foo.lower() == "faq":
            index = 4

        path = "//div[@class='primary-footer']/descendant::a[{0}]".format(index)
        #self.helper.wait_to_execute(5)
        #self.helper.scroll_to_bottom(getLocator("xpath"),path)
        self.helper.click_element(getLocator("xpath"),path)
        #self.helper.wait_to_execute(2)
        self.helper.wait_for_element_visible(getLocator("id"),"NavigationBreadcrumbs",20)
        self.logger.info("Clicked primary footer: {0}".format(foo))
        self.helper.navigation_back()
        self.helper.wait_to_page_load()

    def clickToCorporateFooter(self,foo):
        index = 0
        if foo.lower() == "terms and conditions":
            index = 2
        elif foo.lower() == "privacy guidlines":
            index = 3
        elif foo.lower() == "availability":
            index = 4

        ele = "//ul[@class='corporate-footer__nav']/li[{0}]/a".format(index)
        #self.helper.wait_to_execute(5)
        #self.helper.scroll_to_bottom(getLocator("xpath"), ele)
        self.helper.click_element(getLocator("xpath"), ele)
        self.helper.wait_for_element_visible(getLocator("id"), "NavigationBreadcrumbs", 20)
        #self.helper.wait_to_execute(2)
        self.logger.info("Clicked corporate footer: {0}".format(foo))
        self.helper.navigation_back()

    def clickCookieSettingFooter(self):
        ele = "//ul[@class='corporate-footer__nav']/li/button"
        self.helper.wait_to_execute(2)
        self.helper.scroll_to_bottom(getLocator("xpath"), ele)
        self.helper.click_element(getLocator("xpath"), ele)
        #self.helper.wait_to_execute(2)
        self.logger.info("Clicked cookie setting footer")

    def declineCookieSettingFooter(self):
        self.helper.click_element(getLocator("id"),"evidon-prefdiag-decline")
        self.logger.info("Cookie setting is declined")








