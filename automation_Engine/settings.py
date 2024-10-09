from automation_Engine.base_page import BaseTest

base = BaseTest()
url = base.getEnvValues("Server")
user1 = base.getEnvValues("UserName")
pwd1 = base.getEnvValues("Password")
user2 = base.getEnvValues("User2Name")
pwd2 = base.getEnvValues("User2Password")
fullName1 = base.getEnvValues("UserFullName")
fullName2 = base.getEnvValues("User2FullName")
loginName = base.getEnvValues("LoginName")
loginName2 = base.getEnvValues("User2LoginName")
user_email = base.getEnvValues("UserEmail")
browser = base.configInfo.get("Browser")
tester = base.configInfo.get("Tester")
tester_email = base.configInfo.get("TesterEmail")
