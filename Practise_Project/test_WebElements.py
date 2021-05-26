''' Testcases to test the webelements of webpage
    Tests are verified in Firefox browser (in headless mode), no other browsers are supported
    Warning : Update the geckodriver executable path before execution
    Tests are performed using Pytest
    Author and Tester : Iswarya Murugan '''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import pytest

#Test setup and teardown are defined
@pytest.fixture(scope='class')
def setup(request):
    Firefox_Options = webdriver.FirefoxOptions()
    Firefox_Options.headless = True
    #Change the executable path of geckodriver based on your PC path
    driver = webdriver.Firefox(executable_path="C:\\Learnings\\geckodriver-v0.26.0-win64\\geckodriver.exe",options=Firefox_Options)
    #Get into the website under test
    driver.get("http://www.seleniumframework.com/Practiceform/")
    request.cls.driver = driver
    yield
    driver.close()

#Testfixtures are defined in the class TestWebElements
@pytest.mark.usefixtures('setup')
class TestWebElements():
    #Check the new browser windows gets opened up on clicking the NewBrowserWindow button
    def test_NewBrowserWindow(self,setup):
        self.driver.find_element_by_id("button1").click()
        assert(len(self.driver.window_handles) == 2)
        self.driver.switch_to.window((self.driver.window_handles[1]))
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    # Check the new tab gets opened upon clicking the NewBrowserTab button
    def test_NewBrowserTab(self,setup):
        self.driver.find_element_by_xpath("//button[@onClick='newBrwTab()']").click()
        assert(len(self.driver.window_handles) == 2)
        self.driver.switch_to.window((self.driver.window_handles[1]))
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    #Check the working of alert window, it gets closed upon clicking accept
    def test_NewAlertWorking(self,setup):
        self.driver.find_element_by_css_selector("#alert").click()
        alertWebElement = self.driver.switch_to.alert
        #without the below statement the alert window will not get closed and error will be thrown
        #indirect way of checking the alert windows
        alertWebElement.accept()

    #Check the Form submission by passing no inputs to the form
    def test_FormSubmissionNegativeCase(self,setup):
        self.driver.execute_script("window.scroll(0,1000);")
        self.driver.find_element_by_class_name("dt-btn-submit").click()
        errorText = self.driver.find_element_by_xpath("//div[@class = 'formErrorContent']").text
        assert "This field is required" in errorText

    #Check the form submission by passing all the required input fields
    def test_FormSubmissionPositiveCase(self, setup):
        self.driver.find_element_by_class_name("clear-form").click()
        self.driver.find_element_by_xpath("//input[@name = 'name']").send_keys("Hello")
        self.driver.find_element_by_xpath("//input[@placeholder = 'E-mail *']").send_keys("Hello@gmail.com")
        self.driver.find_element_by_xpath("//input[@name = 'telephone']").send_keys("45789547")
        self.driver.find_element_by_xpath("//input[@name = 'country']").send_keys("Australia")
        self.driver.find_element_by_xpath("//input[@name = 'company']").send_keys("ABC")
        self.driver.find_element_by_xpath("//textarea[@name = 'message']").send_keys("Good website for selenium practice")
        self.driver.find_element_by_class_name("dt-btn-submit").click()
        # The display message getting shown up with some delay so explicit wait is required
        wait = WebDriverWait(self.driver,5)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class = 'formErrorContent']")))
        successText = self.driver.find_element_by_xpath("//div[@class = 'formErrorContent']").text
        assert "Feedback has been sent to the administrator" in successText

    #Check the color change upon single clicking the color change button
    def test_SingleClickColorChange(self,setup):
        self.driver.find_element_by_css_selector("button[id='colorVar']").click()
        changedColor = self.driver.find_element_by_css_selector("button[id='colorVar']").get_attribute('style')
        print(changedColor)
        assert 'color: red' in changedColor

    # Check the color change upon double clicking the color change button
    def test_DoubleClickColorChange(self, setup):
        action = ActionChains(self.driver)
        action.double_click(self.driver.find_element_by_css_selector("button[id='doubleClick']")).perform()
        changedColor = self.driver.find_element_by_css_selector("button[id='doubleClick']").get_attribute('style')
        print(changedColor)
        assert 'color: orange' in changedColor

