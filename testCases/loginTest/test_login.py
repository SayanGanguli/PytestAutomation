from custom_Configuration.base_page import Configuration
from page_Objects.LoginPage import Login


class TestLogin(Configuration):

    def test_login(self):
        login = Login(self.driver)

