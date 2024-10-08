import time
from Automation_Helper.BasePage import BaseEngine
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


class CommonHelper:
    logger = BaseEngine.loggen()

    def __init__(self, driver):
        self.driver = driver
        self.act = ActionChains(driver)

    def load_webpage(self, url):
        self.driver.get(url)
        self.logger.info('The application {0} is launched'.format(url))

    def get_page_title(self):
        title = self.driver.title
        self.logger.info('The page title is {0}'.format(title))
        return title

    def wait_to_page_load(self, waitTime=10):
        self.driver.set_page_load_timeout(waitTime)
        self.logger.info("Waiting to page load")

    def click_element(self, locator_type, locator):
        self.driver.find_element(locator_type, locator).click()
        self.logger.info('Element is clicked at {0}'.format(locator))

    def clear_text_field(self, locator_type, locator):
        self.wait_for_element_visible(locator_type, locator)
        ele = self.driver.find_element(locator_type, locator)
        self.logger.info('Cleared the text in the field {0}'.format(locator))
        ele.clear()

    def enter_text(self, locator_type, locator, value):
        self.wait_for_element_visible(locator_type, locator)
        ele = self.driver.find_element(locator_type, locator)
        self.logger.info('Entered the text in the field {0}'.format(locator))
        ele.send_keys(value)

    def wait_for_element_visible(self, locator_type, locator, duration=10):
        try:
            wait = WebDriverWait(self.driver, duration)
            wait.until(EC.visibility_of_element_located((locator_type, locator)))
            self.logger.info('Element is visible at {0}'.format(locator))

        except TimeoutException:
            self.logger.info('Exception is occurred as element is not found at {0}'.format(locator))
            return False
        return True

    def waitForElementInvisible(self, locator_type, locator, duration):
        try:
            wait = WebDriverWait(self.driver, duration)
            wait.until(EC.invisibility_of_element_located((locator_type, locator)))
            self.logger.info('Element is not visible at {0}'.format(locator))
        except TimeoutException:
            self.logger.info('Exception is occurred as element is found at {0}'.format(locator))
            return False
        return True

    def waitForElementClickable(self, locator_type, locator, duration=10):
        try:
            wait = WebDriverWait(self.driver, duration)
            wait.until(EC.element_to_be_clickable((locator_type, locator)))
            self.logger.info('Element is clickable at {0}'.format(locator))

        except TimeoutException:
            self.logger.info('Element is not clickable at {0}'.format(locator))
            return False
        return True

    def waitForMainPage(self, locator_type, locator):
        self.wait_for_element_visible(locator_type, locator)
        self.logger.info('Wait to land on main UI page {0}'.format(locator))

    def verify_element_present(self, locator_type, locator):
        self.wait_to_execute(2)
        ele = self.driver.find_element(locator_type, locator)
        flag = ele.is_displayed()
        self.logger.info("Element present status is {0}".format(flag))
        return flag

    def select_dropdown(self, locator_type, locator, value):
        drop = Select(self.driver.find_element(locator_type,locator))
        drop.select_by_value(value)

    def click_to_execute(self, locator_type, locator):
        self.wait_for_element_visible(locator_type, locator)
        ele = self.driver.find_element(locator_type, locator)
        self.driver.execute_script("arguments[0].click();", ele)
        self.logger.info('Executing with javascript {0}'.format(locator))

    def focus_on_element(self, locator_type, locator):
        ele = self.driver.find_element(locator_type, locator)
        self.act.move_to_element(ele).perform()
        self.logger.info('Focusing on the element at {0}'.format(locator))

    def mouse_hovering(self, locator_type, locator):
        self.wait_for_element_visible(locator_type, locator)
        ele = self.driver.find_element(locator_type, locator)
        self.act.move_to_element(ele)
        self.logger.info('Mouse hovering on the element at {0}'.format(locator))

    def wait_to_execute(self, waitTime=5):
        time.sleep(waitTime)

    def get_element(self, locator_type, locator):
        ele = self.driver.find_element(locator_type, locator)
        self.logger.info('Fetched the element from location {0}'.format(locator))
        return ele

    def get_element_attribute(self,locator_type, locator, attr):
        ele = self.get_element(locator_type,locator)
        value = ele.get_attribute(attr)
        self.logger.info("{0} is the value for the attribute {1}".format(value,attr))
        return value

    def get_elements(self, locator_type, locator):
        self.wait_for_element_visible(locator_type, locator)
        ele_list = self.driver.find_elements(locator_type, locator)
        self.logger.info('Fetched the list of elements from location {0}'.format(locator))
        return ele_list

    def get_text(self, locator_type, locator):
        self.wait_for_element_visible(locator_type, locator)
        ele = self.driver.find_element(locator_type, locator)
        self.logger.info('Fetched the text of the element from location {0}'.format(locator))
        return ele.text

    def switching_frame(self, locator_type, locator):
        self.logger.info("Now default frame")
        self.wait_to_execute(2)
        self.driver.switch_to.frame(self.driver.find_element(locator_type, locator))
        self.logger.info('Switched to another frame {0}'.format(locator))

    def navigation_back(self):
        self.driver.back()
        self.wait_to_execute(4)
        self.logger.info("Back to the last page")

    def scroll_to_bottom(self,locator_type, locator):
        ele = self.get_element(locator_type,locator)
        view = ele.location_once_scrolled_into_view
        self.logger.info("Scrolled to the bottom of the page")
        return view

    def get_window_handle(self):
        self.logger.info("This is current window")
        return self.driver.current_window_handle

    def get_window_handlers(self, num):
        self.logger.info("Windows:{0}".format(num))
        return self.driver.window_handles[num]

    def switching_window(self, handler):
        self.logger.info("Now default window")
        self.wait_to_execute(2)
        self.driver.switch_to.window(handler)
        self.logger.info('Switched to another window {0}'.format(handler))

    def close_tab(self):
        self.driver.close()

    def press_enter_key(self):
        self.act.send_keys(Keys.ENTER)
        self.act.perform()

    def press_space_key(self):
        self.act.send_keys(Keys.SPACE)
        self.act.perform()

    def refresh_page(self):
        self.driver.refresh()
        self.wait_to_page_load()
