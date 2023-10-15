import logging
import pytest
from pytestsDemo.BaseClass import BaseClass

@pytest.mark.usefixtures("dataload")
class TestExample2(BaseClass):

    def test_editProfile(self, dataload):
        log = self.getlogger()
        log.info(dataload[0])
        log.info(dataload[1])

