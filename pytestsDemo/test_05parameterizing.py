import pytest

# @pytest.mark.skip
def test_crossBrowser(crossbrowser):
    print(crossbrowser)

def test_abhilash(browserMultiValue):
    print(browserMultiValue)
    print(browserMultiValue[1])

@pytest.mark.usefixtures("browserMultiValue")
class TestBrowser:

    def test_abhi(self, browserMultiValue):
        print(browserMultiValue)
        print(browserMultiValue[1])