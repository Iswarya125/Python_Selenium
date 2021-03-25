from selenium import webdriver
from selenium.webdriver import ActionChains

#ActionChains package is not stable, many bugs are reported so not preferred always
driver = webdriver.Firefox(executable_path="C:\\Learnings\\geckodriver-v0.26.0-win64\\geckodriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
action.move_to_element(driver.find_element_by_id("mousehover")).perform()
action.move_to_element(driver.find_element_by_link_text("Top").click()).perform()


