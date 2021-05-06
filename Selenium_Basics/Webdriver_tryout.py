from selenium import  webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox(executable_path="C:\\Learnings\\geckodriver-v0.26.0-win64\\geckodriver.exe")
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
print(driver.title)

driver.find_element_by_xpath("//input[@name='name']").send_keys("Iswarya")
driver.find_element_by_css_selector("[name='email']").send_keys("iswaryamruguan@gmail.com")
driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("Iswarya")
dropdown=Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
#dropdown.select_by_index(0)
driver.find_element_by_css_selector("[type='date']").send_keys("12/05/1994")
driver.find_element_by_css_selector(".btn-success").click()
assert ("success" in driver.find_element_by_class_name("alert-success").text)

driver.maximize_window()
print(driver.current_url)



#below case will work when the tag is defined as <option value="M">
#dropdown.select_by_value("M")

driver.close()

