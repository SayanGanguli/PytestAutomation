import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(autouse=True)
def init_Browser(request, getBrowser):
    global driver
    if getBrowser == "Chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.headless = False
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                  desired_capabilities=DesiredCapabilities.CHROME, options=options)

    elif getBrowser == "Firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                   desired_capabilities=DesiredCapabilities.FIREFOX, options=options)
    else:
        var = None

    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    failed_before = request.session.testsfailed
    yield request.cls.driver
    if request.session.testsfailed != failed_before:
        test_name = request.node.name
        take_screenshot(test_name)
    driver.quit()


def take_screenshot(test_name):
    screenshots_dir = "../PaperTrail/Screenshots/{0}.png".format(test_name)
    driver.save_screenshot(screenshots_dir)


@pytest.fixture(autouse=True)
def getBrowser(request):
    _browser = request.config.getoption("--browser")
    return _browser


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Chrome")
