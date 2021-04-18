from selenium import webdriver

driver = webdriver.Firefox(executable_path="C:\\Learnings\\geckodriver-v0.26.0-win64\\geckodriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#Method 1
#checkboxes = driver.find_elements_by_css_selector("div[id='checkbox-example'] input")
#Method 2
checkboxes = driver.find_elements_by_css_selector("[type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    checkbox.click()
    assert  checkbox.is_selected()

radiobuttons = driver.find_elements_by_class_name("radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

print(driver.find_element_by_id("displayed-text").is_displayed())
driver.find_element_by_id("hide-textbox").click()
print(driver.find_element_by_id("displayed-text").is_displayed())