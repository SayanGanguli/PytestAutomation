from automation_Engine import settings
from automation_Engine.base_page import BaseTest
from automation_Pages.LoginPage import Login


class TestCreatedAsset(BaseTest):

    def asset_portfolio_test(self):
        login = Login(self.driver)
        login.navigateTo(settings.url)
        login.loginApplication(settings.user1, settings.pwd1)

