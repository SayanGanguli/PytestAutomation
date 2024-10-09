from Utility.UtilPage import Util
from pageObjects.loginPage import LoginActivity


class TestLogin(Util):

    def testLogin(self):
        login = LoginActivity(self.driver)
        login.launchApplication(self.readFile("Url"))
        login.selectProduct("papertrail")
        login.loginToApplication(self.readFile("Username"), self.readFile("Password"))
        login.clickSubMenu("Settings", "Profile")
        login.editUsername("software testing")
        login.clickUpdatePreference()
