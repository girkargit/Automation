import pytest
from prac_pytest.baseclass import Baseclass


@pytest.mark.usefixtures("dataload")
class Testecxample3(Baseclass):

    def test_logging(self, dataload):
        log = self.getlogger()
        log.info(dataload[0])
        log.info(dataload[1])
