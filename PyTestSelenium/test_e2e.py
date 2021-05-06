from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from BaseClass import BaseClass


class Testone(BaseClass):
    def test_e2e(self,setup):
        self.driver.find_element_by_link_text("Shop").click()
        products = self.driver.find_elements_by_css_selector("app-card-list[class='row'] app-card")
        for product in products:
            product_name = product.find_element_by_css_selector("div div h4 a").text
            if product_name == "Blackberry":
                product.find_element_by_css_selector("div div button").click()
                break

        self.driver.find_element_by_class_name("btn-primary").click()
        self.driver.find_element_by_css_selector(".btn-success").click()
        self.driver.find_element_by_css_selector("#country").send_keys("Ind")
        wait = WebDriverWait(self.driver,7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//label[@for='checkbox2']").click()
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        assert "Success" in self.driver.find_element_by_class_name("alert-success").text
        self.driver.get_screenshot_as_file("screeshot.png")






