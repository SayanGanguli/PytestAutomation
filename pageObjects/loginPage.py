from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginActivity:
    def __init__(self, driver):
        self.driver = driver

    def launchApplication(self, url):
        self.driver.get(url)

    def solarwinds_Products(self, menu):
        if menu == "appoptics":
            return "product-1"
        elif menu.upper() == "loggly":
            return "product-2"
        elif menu == "papertrail":
            return "product-3"
        elif menu == "pingdom":
            return "product-4"
        else:
            return False

    def selectProduct(self, menu):
        self.driver.find_element(By.ID, self.solarwinds_Products(menu)).click()

    def waitForDashboardPage(self, duration):
        try:
            wait = WebDriverWait(self.driver, duration)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.section")))

        except TimeoutException:
            return False

    def enterUsername(self,uname):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='email']").clear()
        self.driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(uname)

    def enterPassword(self,pwd):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='password']").clear()
        self.driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(pwd)

    def clickButton(self, button):
        self.driver.find_element(By.XPATH, "//button[text()='{0}']".format(button)).click()

    def clickLogInButton(self):
        self.clickButton("Log in")

    def clickUpdatePreference(self):
        self.clickButton("Update Preferences")

    def loginToApplication(self,uname,pwd):
        self.enterUsername(uname)
        self.enterPassword(pwd)
        self.clickLogInButton()

    def clickTopMenu(self, menu):
        #self.waitForDashboardPage(5)
        self.driver.find_element(By.XPATH, "//div[text()='{0}']".format(menu)).click()

    def clickSubMenu(self,menu,subMenu):
        self.clickTopMenu(menu)
        self.driver.find_element(By.XPATH, "//a[text()='{0}']".format(subMenu)).click()

    def editUsername(self, newName):
        self.driver.find_element(By.CSS_SELECTOR,"input[id ='user_name']").clear()
        self.driver.find_element(By.CSS_SELECTOR, "input[id ='user_name']").send_keys(newName)





