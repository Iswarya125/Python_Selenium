from selenium.webdriver.common.by import By

class HomePageFormFiller:

    name = (By.XPATH,"//input[@name='name']")
    email = (By.CSS_SELECTOR,"[name='email']")
    password = (By.XPATH,"//input[@placeholder='Password']")
    date = (By.CSS_SELECTOR,"[type='date']")
    submit_button = (By.CSS_SELECTOR,".btn-success")
    dropdown = (By.ID,"exampleFormControlSelect1")

    def __init__(self,driver):
        self.driver = driver

    def getNameWebElement(self):
        return self.driver.find_element(*HomePageFormFiller.name)

    def getEmailWebElement(self):
        return self.driver.find_element(*HomePageFormFiller.email)

    def getPasswordWebElement(self):
        return self.driver.find_element(*HomePageFormFiller.password)

    def getDateWebElement(self):
        return self.driver.find_element(*HomePageFormFiller.date)

    def getSubmitWebElement(self):
        return self.driver.find_element(*HomePageFormFiller.submit_button)

    def getDropdown(self):
        return self.driver.find_element(*HomePageFormFiller.dropdown)