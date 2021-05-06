from selenium.webdriver.common.by import By

from PageObjectMechanism.Checkoutpage import checkoutpage


class Homepage():
    shop = (By.LINK_TEXT,"Shop");

    def __init__(self,driver):
        self.driver = driver

    def shopItems(self):
        # * -> treats shop as tuple  and deserialize it
        self.driver.find_element(*Homepage.shop).click()
        CheckOutPage = checkoutpage(self.driver)
        return CheckOutPage