import pytest

#scope : if setup and teardown to be called once for a class not for each method inside the class then use scope to define it
@pytest.fixture(scope="class")
def setup():
    print("I am invoked first")
    yield
    #Notice no indentation for lines after yield keyword.
    print("tear down execution")

@pytest.fixture()
def DataSetup():
    print("setting up the data")
    return ["hi","hello","bye"]

@pytest.fixture(params=[("chrome","hi"),("firefox","hello"),("IE","bye")])
#request - to be passed to the fixture function only for paramterized case
# it is an object belongs to fixture
def paramterizingFixture(request):
    return request.param
