from selenium import webdriver

driver = webdriver.Firefox(executable_path="C:\\Learnings\\geckodriver-v0.26.0-win64\\geckodriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_css_selector("#name").send_keys("Hello")
driver.find_element_by_css_selector("input[id='alertbtn']").click()
alert= driver.switch_to.alert
if "Hello" in alert.text:
    alert.accept()
else:
    alert.dismiss()