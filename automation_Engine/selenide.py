import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from automation_Engine.locators import getLocators

class Selenide:

    def __init__(self, driver):
        self.driver = driver
        self.act = ActionChains(driver)

    def navigateTo(self, url):
        self.driver.get(url)

    def refreshBrowser(self):
        self.driver.refresh()

    def navigateToBack(self):
        self.driver.back()

    def getTitle(self):
        return self.driver.title

    def getElement(self, loc_type, location):
        element = self.driver.find_element(getLocators(loc_type), location)
        return element

    def getElementList(self, loc_type, location):
        elements = self.driver.find_elements(getLocators(loc_type), location)
        return elements

    def clickElement(self, loc_type, location):
        self.getElement(loc_type, location).click()

    def clearField(self, loc_type, location):
        self.getElement(loc_type, location).clear()

    def enterText(self, loc_type, location, text):
        self.clearField(loc_type, location)
        self.getElement(loc_type, location).send_keys(text)

    def waitTime(self, duration):
        time.sleep(duration)

    def waitForElementVisible(self, loc_type, location, duration):
        try:
            wait = WebDriverWait(self.driver, duration)
            wait.until(EC.element_to_be_clickable((getLocators(loc_type), location)))

        except TimeoutException:
            return False
        return True

    def verifyVisible(self, loc_type, value):
        return self.getElement(loc_type, value).is_displayed()

    def getElementCount(self, loc_type, location):
        elements = self.getElementList(loc_type, location)
        return len(elements)

    def verifyEnabled(self, loc_type, value):
        return self.getElement(loc_type, value).is_enabled()

    def getCheckedStatus(self, loc_type, value):
        return self.getElement(loc_type, value).is_selected()

    def pressEnter(self, loc_type, value):
        return self.getElement(loc_type, value).send_keys(Keys.ENTER)

    def pressBackspace(self, loc_type, value):
        return self.getElement(loc_type, value).send_keys(Keys.BACKSPACE)

    def focusOnElement(self, loc_type, location):
        element = self.getElement(loc_type, location)
        self.act.move_to_element(element).perform()

    def doubleClick(self, loc_type, location):
        element = self.getElement(loc_type, location)
        self.act.double_click(element)

    def dragAndDropOverTarget(self, source, target):
        self.act.click_and_hold(source).drag_and_drop(source, target).release().perform()

    def dragAndDropToOffset(self, source, offsetX, offsetY):
        self.act.click_and_hold(source).drag_and_drop_by_offset(source, offsetX, offsetY).release().perform()

    def rightClick(self, loc_type, location):
        element = self.getElement(loc_type, location)
        self.act.context_click(element).perform()