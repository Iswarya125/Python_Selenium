from selenium import webdriver

driver = webdriver.Firefox(executable_path="C:\\Learnings\\geckodriver-v0.26.0-win64\\geckodriver.exe")
driver.get("https://the-internet.herokuapp.com/iframe")

#for tags starting with iframe,frame,frameset
#frames are not html elements, so it cannot be accessed using selenium
#They look like part of html, but check the tag if it is frame that needs to handled differently.
# Above is an interview question

#pass frame id, index or name
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_id("tinymce").clear()
driver.find_element_by_id("tinymce").send_keys("hello")
#to switch the driver to regular mode
#this brings out the driver from frame mode to default mode
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)

