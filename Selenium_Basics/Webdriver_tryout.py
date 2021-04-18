from selenium import  webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox(executable_path="C:\\Learnings\\geckodriver-v0.26.0-win64\\geckodriver.exe")
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
print(driver.title)

driver.maximize_window()
print(driver.current_url)

dropdown=Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

#below case will work when the tag is defined as <option value="M">
#dropdown.select_by_value("M")

driver.close()

