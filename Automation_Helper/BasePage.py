import logging
import pytest


@pytest.mark.usefixtures("init_Browser")
class BaseEngine:

    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\Automation.log",
                            filemode='w',format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
