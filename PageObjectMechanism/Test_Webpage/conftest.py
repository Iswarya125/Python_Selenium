from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="firefox")

@pytest.fixture(scope='class')
#request is an instance for the fixture, which is created by python itself, it comes by default.
def setup(request):
    browsername = request.config.getoption("browser_name")
    if browsername == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Learnings\\geckodriver-v0.26.0-win64\\geckodriver.exe")
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()
    elif browsername == "chrome":
        driver = None
    else:
        driver = None
    #below statement i.e return will not work with yield so return driver could not be used here.
    #return driver
    #so below statement is used
    # whichever class using this fixture, if it has driver variable that will be assigned with above created driver
    #here nothing is required to be returned
    #driver will become test class instance attribute, it should be accessed via self.
    request.cls.driver = driver
    yield
    driver.close()



