import pytest

from PageObjectMechanism.TestData.testdatainput import testinputs
from PageObjectMechanism.utilities.BaseClass import BaseClass
from PageObjectMechanism.navigation_helper.HomepageForm import HomePageFormFiller

class Test_WebpageEntries(BaseClass):

    @pytest.fixture(params=testinputs.testdatainputs)
    def input_setup(self,request):
        return request.param

    def test_HomepageForm(self,input_setup):
        HomepageformfillerObj = HomePageFormFiller(self.driver)
        HomepageformfillerObj.getNameWebElement().send_keys(input_setup['FirstName'])
        HomepageformfillerObj.getEmailWebElement().send_keys(input_setup['Email'])
        HomepageformfillerObj.getPasswordWebElement().send_keys(input_setup['Password'])
        Gender = input_setup['Gender']
        Dropdownlocator = HomepageformfillerObj.getDropdown()
        self.selectBasedOnText(Dropdownlocator,Gender)
        HomepageformfillerObj.getDateWebElement().send_keys(input_setup['DOB'])
        HomepageformfillerObj.getSubmitWebElement().click()
        assert ("success" in self.driver.find_element_by_class_name("alert-success").text)
        self.driver.refresh()

