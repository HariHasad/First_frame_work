import inspect
import logging

import pytest

@pytest.mark.usefixtures("setup")
class Baseclass:
 def getLogger(self):
        # For logger
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)  # Object for filehandler
        logger.setLevel(logging.DEBUG)
        return logger
