import pytest
@pytest.mark.usefixtures("dataload") # return data from fixture which used for test case
class TestExample2:

    def test_editProfile(self, dataload):
        print(dataload)
        print(dataload[0])
        print(dataload[1])

