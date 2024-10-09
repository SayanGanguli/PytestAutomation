import logging

from automation_Engine.base_page import BaseTest
from automation_Pages.DashboadPage import DashBoard


class Login(DashBoard):
    log = BaseTest.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)

    def navigateTo(self, url):
        self.selenide.navigateTo(url)
        self.log.info("Launched Application")

    def loginApplication(self, uname, pwd):
        self.enterUserName(uname)
        self.enterPassword(pwd)
        self.clickSignIn()
        self.log.info("Login to the application")

    def enterUserName(self, uname):
        self.selenide.enterText("id", "username", uname)
        self.selenide.waitTime(1)
        self.log.info("Entered Username")

    def enterPassword(self, password):
        self.selenide.enterText("id", "password", password)
        self.selenide.waitTime(1)
        self.log.info("Entered Password")

    def clickSignIn(self):
        self.selenide.clickElement("css", "button[type = 'submit']")
        self.selenide.waitTime(20)
        self.log.info("Clicked SignIn Button")
