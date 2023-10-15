import logging
def test_loggingDemo():
    logger = logging.getLogger(__name__) # --name-- = atruntime capture file name

    filehandler = logging.FileHandler("logfile.log") # Have to pass file name
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s") # File formatting
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler) # filehandler object and filhandler nothing but file location
    logger.setLevel(logging.ERROR) # It will print from warning to error onwords and basically set the level

    logger.debug("A debug statment is executed.")
    logger.info("Information statment.")
    logger.warning("Something is in warning mode.")
    logger.error("A Major error.")
    logger.critical("Critical issue")
