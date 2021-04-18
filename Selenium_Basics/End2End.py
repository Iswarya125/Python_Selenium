from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox(executable_path="C:\\Learnings\\geckodriver-v0.26.0-win64\\geckodriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_link_text("Shop").click()
products = driver.find_elements_by_css_selector("app-card-list[class='row'] app-card")
for product in products:
    product_name = product.find_element_by_css_selector("div div h4 a").text
    if product_name == "Blackberry":
        product.find_element_by_css_selector("div div button").click()
        break

driver.find_element_by_class_name("btn-primary").click()
driver.find_element_by_css_selector(".btn-success").click()
driver.find_element_by_css_selector("#country").send_keys("Ind")
wait = WebDriverWait(driver,7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//label[@for='checkbox2']").click()
driver.find_element_by_xpath("//input[@type='submit']").click()
assert "Success" in driver.find_element_by_class_name("alert-success").text
driver.get_screenshot_as_file("screeshot.png")


