import logging

from custom_Configuration.base_page import Configuration
from page_Objects.HomePage import HomePage


class Login(HomePage):
    log = Configuration.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)

    def navigateTo(self, url):
        self.selenide.navigateTo(url)
        self.log.info("Launched Application")

    def loginApplication(self, uname, pwd):


    def enterUserName(self, uname):


    def enterPassword(self, password):


    def clickSignIn(self):
