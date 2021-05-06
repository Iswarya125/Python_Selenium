from PageObjectMechanism.navigation_helper.Homepage import Homepage
from PageObjectMechanism.utilities.BaseClass import BaseClass


class Testone(BaseClass):
    def test_e2e(self,setup):

        homepage = Homepage(self.driver)
        CheckOutPage = homepage.shopItems()
        products = CheckOutPage.getCardtitle()

        i = -1
        for product in products:
            i = i+1
            product_name = product.text
            if product_name == "Blackberry":
                CheckOutPage.getCardFooter()[i].click()
                break

        Confirmpage = CheckOutPage.getbutton()

        Confirmpage.getSuccessbutton().click()
        Confirmpage.getCountry().send_keys("Ind")
        self.verifyLinkPresence("India")
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//label[@for='checkbox2']").click()
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        assert "Success" in self.driver.find_element_by_class_name("alert-success").text
        self.driver.get_screenshot_as_file("screeshot.png")






