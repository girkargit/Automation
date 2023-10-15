import pytest

@pytest.mark.usefixtures("setup", "dataload")
class Testexapmle:
    def test_fixturedemo(self):
        print("i will be execute steps in fixture demo methode.")

    def test_fixturedemo1(self):
        print("i will be execute steps in fixture demo methode.")

    def test_fixturedemo2(self):
        print("i will be execute steps in fixture demo methode.")

    def test_fixturedemo3(self, dataload):
        print("i will be execute steps in fixture demo methode.", dataload)