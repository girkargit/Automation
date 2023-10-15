import inspect
import logging

class Baseclass:
    def getlogger(self):
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)  # --name-- = atruntime capture file name
        filehandler = logging.FileHandler("logfile.log")  # Have to pass file name
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")  # File formatting
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)  # filehandler object and filhandler nothing but file location
        logger.setLevel(logging.DEBUG)  # It will print from warning to error onwords and basically set the level
        return logger
