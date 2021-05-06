import  pytest

#Inherited derived class need not mention this fixture each time, as the base class has the required knowledge.
@pytest.mark.usefixtures('setup')
class BaseClass:
    pass