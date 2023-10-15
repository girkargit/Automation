import pytest

@pytest.mark.skip
def test_prog():
    msg = "hellow"
    assert msg == 'hii' , "test fail, condition not match."

@pytest.mark.smoke
def test_credit(setup):
    a = 4
    b = 6
    assert a + 2 == b

def test_crossbrowser(crossbrowser, dataload):
    print(crossbrowser, dataload)

