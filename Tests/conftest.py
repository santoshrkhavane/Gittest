import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome",
    )
@pytest.fixture(scope="class")
def setup(request):
    global driver
    browserName= request.config.getoption("browser_name")
    if browserName == "Chrome":
        obj = Service("C:\\software\\chromedriver.exe")
        driver = webdriver.Chrome(service=obj)
    elif browserName == "firefox":
        obj = Service("C:\\software\\geckodriver.exe")
        driver = webdriver.Firefox(service=obj)
    elif browserName == "Edge":
        obj = Service("C:\\software\\msedgedriver.exe")
        driver = webdriver.Edge(service=obj)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver

