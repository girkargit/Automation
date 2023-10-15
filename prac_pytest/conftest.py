import pytest

@pytest.fixture(scope="class")
def setup():
    print("i will be executing first.")
    yield
    print("i will be executed last.")

@pytest.fixture()
def dataload():
    print("user profile data is being created.")
    return ["rahul", "shetty", "rahulshettyacademy.com"]

@pytest.fixture(params= [("chrome", "rahul"), ("firefox", "shetty")])
def crossbrowser(request):
    return request.param