import os.path
import time
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome import service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope="class", autouse=True)
def init_Browser(request, getBrowser):
    global driver
    if getBrowser == "Chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument("--disable-notifications")
        webdriver_service = service.Service(ChromeDriverManager().install())
        webdriver_service.start()
        driver = webdriver.Remote(webdriver_service.service_url, options=options)

    elif getBrowser == "Edge":
        options = webdriver.EdgeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument("--disable-notifications")
        webdriver_service = service.Service(EdgeChromiumDriverManager().install())
        webdriver_service.start()
        driver = webdriver.Remote(webdriver_service.service_url, options=options)

    else:
        print("No browser is open")

    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    failed_Test = request.session.testsfailed
    yield request.cls.driver
    if request.session.testsfailed != failed_Test:
        test_name = request.node.name
        take_screenshot(test_name)
    driver.quit()


def take_screenshot(test_name):
    screenshots_dir = "E://Documents//Pytest//CanonB2BModel//Screenshots{0}.png".format(test_name)
    driver.save_screenshot(screenshots_dir)


def pytest_html_report_title(report):
    report.title = "CANON B2B"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    now = datetime.now()
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            report_dir = os.path.dirname(item.config.option.htmlpath)
            file_name = str(int(round(time.time() * 1000))) + ".png"
            destination_file = os.path.join(report_dir, file_name)
            driver.save_screenshot(destination_file)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extras.append(pytest_html.extras.html(html))
            report.extras = extras


@pytest.fixture(scope="class", autouse=True)
def getBrowser(request):
    _browser = request.config.getoption("--browser")
    return _browser


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Chrome")
