import time

from selenium import webdriver

driver = webdriver.Firefox(executable_path="C:\\Learnings\\geckodriver-v0.26.0-win64\\geckodriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#global wait applicable to all the driver calls in this file wherever driver object is used.
# it waits for 5sec or until the driver object is returned whichever is earlier
driver.implicitly_wait(5)


driver.find_element_by_css_selector(".search-keyword").send_keys("ber")
#If below sleep is removed, not working out
time.sleep(4)

elements = driver.find_elements_by_css_selector("div[class='product-action'] button")
#elements = driver.find_elements_by_xpath("//div[@class='product-action']/button")
print(len(elements))
for element in elements:
    element.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()
print(driver.find_element_by_class_name("promoInfo").text)
