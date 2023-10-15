import pytest

@pytest.mark.usefixtures("dataload")
class Testecxample2:

    def test_editprofile(self, dataload):
        for i in dataload:
            print(i, end=" ")
