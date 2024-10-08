from Automation_Helper.BasePage import BaseEngine
from Automation_Helper.HelperPage import CommonHelper
from Automation_Helper import Locators
from Automation_Helper.Locators import getLocator
from Automation_Helper.UI_Operations import UIOperations


class Registration(UIOperations):
    logger = BaseEngine.loggen()

    def __init__(self, driver):
        super().__init__(self)
        self.helper = CommonHelper(driver)

    def registerNewUser(self):
        self.helper.click_element(getLocator("xpath"), Locators.register_link)
        self.logger.info("Clicked Register Button")

    ##### 1st Page of Registration #####

    def selectCountry(self, country):
        self.helper.wait_for_element_visible(getLocator("xpath"), Locators.select_country_ddn)
        self.helper.click_element(getLocator("xpath"), Locators.select_country_ddn)
        self.logger.info("Country dropdown is open")
        self.helper.wait_to_execute(1)
        self.selectAnOption(country)
        self.logger.info("Country {0} is selected".format(country))
        self.helper.wait_to_execute(1)

    def selectLanguage(self, language):
        self.helper.wait_for_element_visible(getLocator("xpath"), Locators.select_language_ddn)
        self.helper.click_element(getLocator("xpath"), Locators.select_language_ddn)
        self.logger.info("Language dropdown is open")
        self.helper.wait_to_execute(1)
        self.selectAnOption(language)
        self.logger.info("Language {0} is selected".format(language))
        self.helper.wait_to_execute(1)

    def clickStepButton(self, direction):
        self.clickButton_Text(direction)
        self.helper.wait_to_execute(3)

    ##### 2nd Page of Registration #####

    def enterNewUserEmail(self, new_mail):
        self.logger.info("New Email: {0}".format(new_mail))
        self.enterInputFields("NewUser", new_mail)
        self.helper.wait_to_execute(2)

    def clickCheckBoxes(self, field):
        self.clickFieldText(field)
        self.logger.info("Checkbox {0} is selected".format(field))
        self.helper.wait_to_execute(3)

    ##### 3rd Page of Registration #####

    def clickDDNForDetails(self, ddn, ddn_value):
        if ddn.lower() == "salutation":
            ddn = "salutation"
        elif ddn.lower() == "area":
            ddn = "areaCodeName"
        self.helper.wait_to_execute(2)
        self.clickButton_DDN(ddn)
        self.clickFieldText(ddn_value)

    def enterPrimaryContactDetails(self):
        self.clickDDNForDetails("Salutation", "Mr")
        self.enterInputFields("First Name", "Auto")
        self.enterInputFields("Last Name", "Tester")
        self.enterInputFields("Phone", "8987654321")
        self.enterInputFields("Job Title", "SE")
        self.clickDDNForDetails("Area", "47-Norway")

    ##### 4th Page of Registration #####
    def enterBusinessDetails(self):
        self.enterInputFields("Company", "Marvel")
        self.enterInputFields("Address", "21 Park Street")
        self.enterInputFields("Postal Code", "12345")
        self.enterInputFields("Company City", "Oslo")

    ##### Final Page of Registration #####

    def expandSummaryPage(self, section):
        self.helper.wait_to_page_load()
        self.clickFieldText(section)
        self.logger.info("Expanded the section: " + section)
