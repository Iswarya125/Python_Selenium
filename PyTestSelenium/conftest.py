from selenium import webdriver
import pytest

@pytest.fixture(scope='class')
def setup(req ):
    driver = webdriver.Firefox(executable_path="C:\\Learnings\\geckodriver-v0.26.0-win64\\geckodriver.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice/")