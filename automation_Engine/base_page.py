import inspect
import json
import logging
import pytest


@pytest.mark.usefixtures("init_Driver")
class BaseTest:
    customConfig = {}
    configInfo = {}

    @staticmethod
    def customLogger(self, logLevel=logging.DEBUG):
        # Gets the name of the class / method from where this method is called
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        # By default, log all messages
        logger.setLevel(logging.DEBUG)

        fileHandler = logging.FileHandler("..//IIS-Zephyr//Logs//automation.log", mode='w')
        fileHandler.setLevel(logLevel)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

        return logger

    def readFile(self):
        with open("..//IIS-Zephyr//automation_Engine//environment.json", "r") as env:
            read_file = json.load(env)
            return read_file

    def getEnvValues(self, param):
        data = self.readFile()
        self.configInfo.update(data)
        envValue = self.configInfo.get("Environment")
        self.customConfig.update(self.configInfo.get(envValue))
        return self.customConfig.get(param)

    def getMaxElementWaitTime(self):
        return self.configInfo.get("MaxElementWaitTime")




