import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox(executable_path="C:\\Learnings\\geckodriver-v0.26.0-win64\\geckodriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")


driver.find_element_by_css_selector(".search-keyword").send_keys("ber")
#If below sleep is removed, not working out
time.sleep(4)

Items_selected=[]
elements = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for element in elements:
    Items_selected.append(element.find_element_by_xpath("parent::div/parent::div/h4").text)
    element.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

wait = WebDriverWait(driver,8)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoCode")))

In_cart =[]
In_cart_names = []
In_cart= driver.find_elements_by_css_selector(".product-name")
for element in In_cart:
    In_cart_names.append(element.text)

assert  Items_selected == In_cart_names

Initial_amnt = driver.find_element_by_css_selector(".discountAmt").text
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()


wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoInfo")))
discounted_amnt = driver.find_element_by_css_selector(".discountAmt").text

assert  float(Initial_amnt) > float(discounted_amnt)

prices = driver.find_elements_by_xpath("//tr/td[5]/p")
sum = 0
for price in prices:
    sum += int(price.text)

calculated_value = int(driver.find_element_by_class_name("totAmt").text)
assert sum ==calculated_value