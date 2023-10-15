# mentor@rahulshettyacademy.com
import pytest
# # Fixture run before any test execution we have to pass to the methode as argument. Then always befor test methode.
# @pytest.fixture()
# def setup():
#     print("I will be executing first.")
#     yield  # After yeild what ever the run after run test case
#     print("I will be executing last.")

def test_fixtureDemo1(setup):
    print("I will execute steps in fixtureDemo methode.")

@pytest.mark.usefixtures("setup") # Automatically apply to the all methode inside the class
class TestExample:
    def test_fixtureDemo0(self):
        print("I will execute steps in fixtureDemo methode.")

    def test_fixtureDemo2(self):
        print("I will execute steps in fixtureDemo methode.")

    def test_fixtureDemo3(self):
        print("I will execute steps in fixtureDemo methode.")

    def test_fixtureDemo4(self):
        print("I will execute steps in fixtureDemo methode.")