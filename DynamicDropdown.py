from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="C:\\Learnings\\geckodriver-v0.26.0-win64\\geckodriver.exe")
#driver.get("https://www.makemytrip.com/")
#driver.find_element_by_id("fromCity").click()
#driver.find_element_by_xpath("//label[@for='fromCity']/input").send_keys("Co")
#time.sleep(5)
#list_places = driver.find_elements_by_id("react-autowhatever-1-section-0-item-0")
#print(len(list_places))
#for place in list_places:
#    if "Coimbatore" in place.text:
#        place.click()
#        break


driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_id("autosuggest").send_keys("Ind")
time.sleep(2)
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break

#here .text will not workout as this value is not a static one, Selenium reads through the webpage
#and loads all the text initially that can be fetched using .text but here we are choosing the  value dynamically
#so .get_attribute is used
assert driver.find_element_by_id("autosuggest").get_attribute('value') == "India"

