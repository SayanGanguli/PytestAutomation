from Automation_Helper.BasePage import BaseEngine
from Automation_Helper.HelperPage import CommonHelper
from Automation_Helper.Locators import getLocator


class UIOperations:
    logger = BaseEngine.loggen()

    def __init__(self, driver):
        self.helper = CommonHelper(driver)

    def enterInputFields(self, field, value):
        loc = ""
        if field.lower() == "username":
            loc = "username"
        elif field.lower() == "password":
            loc = "inputPasswordSecret"
        elif field.lower() == "newuser":
            loc = "email"
        elif field.lower() == "search":
            loc = "Ntt"
        elif field.lower() == "yopmail":
            loc = "login"
        elif field.lower() == "first name":
            loc = "conFirstName"
        elif field.lower() == "last name":
            loc = "conLastName"
        elif field.lower() == "phone":
            loc = "conPhoneNumber"
        elif field.lower() == "job title":
            loc = "conJobTitle"
        elif field.lower() == "company":
            loc = "companyId"
        elif field.lower() == "address":
            loc = "businessCompanyAddress"
        elif field.lower() == "postal code":
            loc = "businessCompanyPostalCode"
        elif field.lower() == "company city":
            loc = "businessCompanyCity"
        elif field.lower() == "company":
            loc = "companyId"
        elif field.lower() == "address1":
            loc = "address1"
        elif field.lower() == "address2":
            loc = "address2"
        elif field.lower() == "address3":
            loc = "address3"
        elif field.lower() == "city":
            loc = "city"
        elif field.lower() == "post":
            loc = "postalCode"
        elif field.lower() == "phone number":
            loc = "phoneNumber"

        self.helper.enter_text(getLocator("xpath"), "//input[@name='{0}']".format(loc), value)
        self.logger.info("Entered " + loc + ": " + value)

    def clickFieldText(self, field):
        self.helper.wait_for_element_visible(getLocator("xpath"), "//span[text()='{0}']".format(field))
        self.helper.click_element(getLocator("xpath"), "//span[text()='{0}']".format(field))

    def clickButton_DDN(self, option):
        self.helper.wait_to_execute(1)
        self.helper.focus_on_element(getLocator("xpath"), "//button[@name='{0}']".format(option))
        self.helper.wait_for_element_visible(getLocator("xpath"), "//button[@name='{0}']".format(option))
        self.helper.click_element(getLocator("xpath"), "//button[@name='{0}']".format(option))

    def selectAnOption(self, field):
        self.helper.focus_on_element(getLocator("xpath"), "//span[@title ='{0}']".format(field))
        self.helper.wait_for_element_visible(getLocator("xpath"), "//span[@title ='{0}']".format(field))
        self.helper.click_element(getLocator("xpath"), "//span[@title ='{0}']".format(field))

    def clickButton_Text(self, button):
        self.helper.wait_for_element_visible(getLocator("xpath"), "//button[text()='{0}']".format(button))
        self.helper.click_element(getLocator("xpath"), "//button[text()='{0}']".format(button))

    def backToPage(self):
        self.helper.navigation_back()
