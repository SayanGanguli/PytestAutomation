import logging

from automation_Engine.base_page import BaseTest
from automation_Engine.selenide import Selenide


class DashBoard:
    log = BaseTest.customLogger(logging.DEBUG)
    """"/*** GLOBAL VARIABLE" *****/ """
    welMenu = "//li/a[@class='dropdown-toggle welcome-user']"

    def __init__(self, driver):
        self.driver = driver
        self.selenide = Selenide(driver)

    def openWelcomeMenu(self):
        path = "//li/a[@class='dropdown-toggle welcome-user']"
        self.selenide.clickElement("xpath", path)
        self.log.info("Click on Welcome Panel")
        self.selenide.waitTime(1)

    def clickLogout(self):
        self.openWelcomeMenu()
        self.selenide.clickElement("id", "sessionStatus")
        self.log.info("Logout From The Application")

    def waitForUsername(self, duraton):
        self.selenide.waitForElementVisible("css", "span.user-welcome-name", duraton)

    def leftNavigationMenu(self, menu=""):
        if menu.upper() == "ASSET ALLOCATION":
            return "nav-aa"
        elif menu.upper() == "ASSET ANALYSIS":
            return "nav-mam"
        elif menu.upper() == "ATTRIBUTION ANALYSIS":
            return "nav-attb"
        elif menu.upper() == "CREATE A PORTFOLIO":
            return "nav-pc"
        else:
            return False

    def clickModule(self, menu, loc_type="id"):
        self.selenide.clickElement(loc_type, self.leftNavigationMenu(menu))
        self.log.info("Navigate to " + menu)
        self.selenide.waitTime(5)

    def actionOnDeletePopUp(self, act):
        self.selenide.clickElement("xpath",
                                   "//div[contains(@style,'display: block;')]/descendant::button[text()='{0}']".format(
                                       act))
        self.log.info("Click on Button of Pop-up of Delete" + act)
        self.selenide.waitTime(2)

    def clickTopMenu(self, menu):
        self.selenide.clickElement("xpath", "//a/span[normalize-space()='{0}']".format(menu))
        self.log.info("Click on Top Menu: " + menu)
        self.selenide.waitTime(2)
