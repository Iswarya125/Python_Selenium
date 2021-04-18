from selenium import webdriver

driver = webdriver.Firefox(executable_path="C:\\Learnings\\geckodriver-v0.26.0-win64\\geckodriver.exe")
driver.get("https://the-internet.herokuapp.com/windows")
driver.implicitly_wait(5)
driver.find_element_by_link_text("Click Here").click()
#window_handles - holds the webpages opened by selenium
#0th index refers to first opened page
#1st index refers to second opened page
#Pass the page address to switch_to.window so that driver will get navigates to required page
driver.switch_to.window(driver.window_handles[1])
driver.implicitly_wait(5)
print(driver.find_element_by_tag_name("h3").text)
driver.close()

driver.switch_to.window(driver.window_handles[0])
print(driver.find_element_by_tag_name("h3").text)