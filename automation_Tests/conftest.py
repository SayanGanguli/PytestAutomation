import os
import time
import platform
from platform import python_version
import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from automation_Engine import settings


@pytest.fixture(autouse=True)
def init_Driver(request, getBrowser):
    global driver
    if getBrowser == "Chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-notifications")
        # options.add_argument("enable-automation")
        options.add_argument("no-sandbox")
        options.add_argument("--disable-gpu")
        options.headless = False
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                  desired_capabilities=DesiredCapabilities.CHROME, options=options)

    elif getBrowser == "Firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--disable-infobar")
        options.add_argument("no-sandbox")
        options.headless = False
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                   desired_capabilities=DesiredCapabilities.FIREFOX, options=options)
    else:
        driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())

    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(5)
    request.cls.driver = driver

    failed_before = request.session.testsfailed
    yield request.cls.driver
    if request.session.testsfailed != failed_before:
        test_name = request.node.name
        take_screenshot(test_name)
    driver.quit()


def take_screenshot(test_name):
    screenshots_dir = "..//IIS-Zephyr//Screenshots//{0}.png".format(test_name)
    driver.save_screenshot(screenshots_dir)


def pytest_html_report_title(report):
    report.title = "IIS-ZEPHYR AUTOMATION"


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        extra.append(pytest_html.extras.url(settings.url))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = str(int(round(time.time() * 1000))) + ".png"
            # file_name = report.nodeid.replace("::", "_") + ".png"
            destinationFile = os.path.join(report_directory, file_name)
            driver.save_screenshot(destinationFile)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
            report.extra = extra


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=settings.browser)


@pytest.fixture(autouse=True)
def getBrowser(request):
    _browser = request.config.getoption("--browser")
    return _browser


def pytest_configure(config):
    ''' modifying the table pytest environment'''
    config._metadata.pop("Plugins")
    py_version = python_version()
    pl_version = platform.platform()

    # overwriting old parameters with  new parameters
    config._metadata = {
        "Tester": settings.tester,
        "Tester Email": settings.tester_email,
        "Python": py_version,
        "Platform": pl_version,
        "Browser": settings.browser
    }
