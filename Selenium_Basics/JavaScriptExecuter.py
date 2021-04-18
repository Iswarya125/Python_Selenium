from selenium import webdriver

driver = webdriver.Firefox(executable_path="C:\\Learnings\\geckodriver-v0.26.0-win64\\geckodriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_css_selector("input[name='name']").send_keys("hello")
#value attribute is not exposed but still we can use it - applicable only for value attribute
print(driver.find_element_by_css_selector("input[name='name']").get_attribute("value"))
#another way to do the above - try out in firefox console
print(driver.execute_script("return document.getElementsByName('name')[0].value"))
Shopper_element = driver.find_element_by_css_selector("[href*='shop']")
#Click using javascript
# pass the webelements from second arguments on, arguments[0] - represents first element i.e Shopper_element
#arguments[1] represents next one is empty below but we can pass any number of arguments
driver.execute_script("arguments[0].click();",Shopper_element)
#To scroll using javascript executor
driver.execute_script("window.scroll(0,document.body.scrollHeight);")