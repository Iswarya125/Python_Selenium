from selenium.webdriver.common.by import By


class confirmpage:

    successbutton = (By.CSS_SELECTOR,".btn-success")
    countrywebelement = (By.CSS_SELECTOR,"#country")

    def __init__(self,driver):
        self.driver = driver

    def getSuccessbutton(self):
        return self.driver.find_element(*confirmpage.successbutton)

    def getCountry(self):
        return self.driver.find_element(*confirmpage.countrywebelement)