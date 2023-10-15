# Any pytest file must be start with test_ and ends with _test
# Pytest methode (function) should start with test
# Any code should be wrapped in methode only
# Methode name should have sense
# -k stand for methode name execution all test cases having addition text eg. py.test -k addition -v -s
# -s stand for logs in out put eg. py.test -v -s
# -v stand for more information metadata eg . py.test -v
# You can run specific file with py.test <file name> eg. py.test test_02demo.py -v -s
# You can mark ( tag ) @pytest.mark.smoke and then run with -m eg. py.test -m smoke -v -s
# You can skip test using @pytest.mark.skip --> default
# @pytest.mark.xfail ( Do not showing failing test case in our report in short skiping result in report)
import pytest


@pytest.mark.smoke
def test_firstprog(setup):
    print("Hello world")

@pytest.mark.xfail
def test_taskCreditCard():
    print("Good Morning")

