from selenium.webdriver.common.by import By

from PageObjectMechanism.Confirmpage import confirmpage


class checkoutpage:

    cardtitle = (By.CSS_SELECTOR,"app-card-list[class='row'] app-card")
    cardfooter = (By.CSS_SELECTOR,"div div button")
    buttonclick = (By.CLASS_NAME,"btn-primary")

    def __init__(self,driver):
        self.driver = driver

    def getCardtitle(self):
        return self.driver.find_elements(*checkoutpage.cardtitle)

    def getCardFooter(self):
        return  self.driver.find_elements(*checkoutpage.cardfooter)

    def getbutton(self):
        self.driver.find_element(*checkoutpage.buttonclick).click()
        Confirmpage = confirmpage(self.driver)
        return Confirmpage