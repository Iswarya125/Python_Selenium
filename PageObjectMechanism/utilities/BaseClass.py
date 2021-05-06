import  pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



#Inherited derived class need not mention this fixture each time, as the base class has the required knowledge.
@pytest.mark.usefixtures('setup')
class BaseClass:
    def verifyLinkPresence(self,text):
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectBasedOnText(self,locator,text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)
