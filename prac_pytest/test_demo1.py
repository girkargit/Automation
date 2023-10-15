import pytest
def test_firstprogm():
    print("hellow")

@pytest.mark.smoke
def test_creditcard():
    print("Hiiiiiiiii")

@pytest.mark.xfail
def test_bank():
    print("good morning")