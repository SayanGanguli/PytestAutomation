from selenium.webdriver.common.by import By


def getLocators(by_locator=""):
    if by_locator.lower() == "xpath":
        return By.XPATH
    elif by_locator.lower() == "css":
        return By.CSS_SELECTOR
    elif by_locator.lower() == "id":
        return By.ID
    elif by_locator.lower() == "class":
        return By.CLASS_NAME
    elif by_locator.lower() == "name":
        return By.NAME
    else:
        return False
