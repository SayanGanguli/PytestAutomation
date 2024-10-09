from automation_Engine.base_page import BaseTest
from automation_Pages.LoginPage import Login
from automation_Engine import settings


class TestLogin(BaseTest):

    def test_login(self):
        login = Login(self.driver)
        login.navigateTo(settings.url)
        login.loginApplication(settings.user1, settings.pwd1)
        login.clickLogout()
