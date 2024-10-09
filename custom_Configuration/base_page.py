import inspect
import json
import logging
import pytest


@pytest.mark.usefixtures("init_Driver")
class Configuration:
    customConfig = {}
    configInfo = {}

    @staticmethod
    def customLogger(logLevel=logging.DEBUG):
        # Gets the name of the class / method from where this method is called
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        # By default, log all messages
        logger.setLevel(logging.DEBUG)

        fileHandler = logging.FileHandler("..//MakeMyTrip//Logs//automation.log", mode='w')
        fileHandler.setLevel(logLevel)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

        return logger

    @staticmethod
    def getApplicationDetails(param):
        with open("../../MakeMyTrip/custom_Configuration/environment.json", "r") as env:
            read_file = json.load(env)
            return read_file.get(param)