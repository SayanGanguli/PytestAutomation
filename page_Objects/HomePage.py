import logging

from custom_Configuration.base_page import Configuration
from custom_Configuration.selenide import Selenide


class HomePage:
    log = Configuration.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
        self.selenide = Selenide(driver)
