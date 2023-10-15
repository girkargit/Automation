import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_prog():
    msg = "Hellow"
    assert msg  == "Hii", "Test fails because string do not match."


def test_additionCreditCard():
    a = 4
    b = 6
    assert a + 2 == 6 , "Addition do not match."


