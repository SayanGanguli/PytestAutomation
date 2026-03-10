import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.options import Options


@pytest.fixture(params=["chrome", "edge"], scope="module", autouse=True)
def setUp(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        # options.add_argument("headless")
        options.add_argument("--disable-dev-sh-launching")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    elif request.param == "edge":
        options = Options()
        options.add_argument("--start-maximized")
        # options.add_argument("headless")
        # service = Service(EdgeChromiumDriverManager().install())
        service = Service("D:/Workspace/Demo Pytest/PytestAutomation/msedgedriver.exe")
        driver = webdriver.Edge(service=service, options=options)

    else:
        raise ValueError(f"Unsupported browser: {request.param}")

    driver.get("https://testautomationpractice.blogspot.com/")
    driver.implicitly_wait(15)
    yield driver
    driver.quit()