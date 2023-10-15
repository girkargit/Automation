import pytest
# Fixture run before any test execution we have to pass to the methode as argument. Then always befor test methode.
'''
conftest file which is the file where fixture is define and this firxture applicable to the
all pytest file (start with test) in that folder. 
'''
'''
if we want to apply fixture to starting at the class to the end of the class
then we have to pass scope="class"
@pytest.fixture(scope="class")
'''
@pytest.fixture(scope="class")
def setup():
    print("I will be executing first.")
    yield  # After yeild what ever the run after run test case
    print("I will be executing last.")

@pytest.fixture()
def dataload():
    print("User profile data being created")
    return ["Abhilash", "Girkar", "abhilash.com"]

@pytest.fixture(params=["chrome", "Firefox","IE"]) # parameterizing in this param if we call this fixture then test case will three time
def crossbrowser(request):
    return request.param

@pytest.fixture(params=[("chrome", "abhilash", "girkar"),("firefox", "suraj", "pasthe"), ("IE", "omkar", "hundre")])
def browserMultiValue(request): # in this param if we call this fixture then test case will three time
    return request.param

