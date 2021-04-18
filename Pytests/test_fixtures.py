import  pytest
from Pytests.loggingClass import logging_base

def test_fixturetryout(setup):
    print("test execution")

class Testexample:
    def test_fixturetryout1(setup):
        print("test execution1")

    def test_fixturetryout2(setup):
        print("test execution2")

@pytest.mark.usefixtures('setup')
class Testexample1():
    def test_fixturetryout1(self):
        logger1 = logging_base()
        logger1.getlogger().warn("warning")
        print("test execution1")

    def test_fixturetryout2(self):
        print("test execution2")

@pytest.mark.usefixtures("DataSetup")
class Testexample2:
    def test_fixturetryout1(self,DataSetup):
        print(DataSetup[0])

#3 times executed with tuples in the list passed from conftest file (parameterizingFixture)
def test_exampleParameterized(paramterizingFixture):
    print(paramterizingFixture[0])
    print(paramterizingFixture[1])