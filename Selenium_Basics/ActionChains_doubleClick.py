from selenium import webdriver
from selenium.webdriver import ActionChains

#ActionChains package is not stable, many bugs are reported so not preferred always
driver = webdriver.Firefox(executable_path="C:\\Learnings\\geckodriver-v0.26.0-win64\\geckodriver.exe")
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)
#for double clicking
action.double_click(driver.find_element_by_id("double-click")).perform()
#for right clicking
action.context_click(driver.find_element_by_id("double-click")).perform()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()