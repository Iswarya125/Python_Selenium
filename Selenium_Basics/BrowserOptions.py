from selenium import webdriver

Firefox_Options = webdriver.FirefoxOptions()
Firefox_Options.headless= True
driver = webdriver.Firefox(executable_path="C:\\Learnings\\geckodriver-v0.26.0-win64\\geckodriver.exe",options=Firefox_Options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)