import json
import pytest


@pytest.mark.usefixtures("init_Browser")
class Util:
    configInfo = {}

    def readFile(self, param):
        env_Path = "../Papertrail/Configuration/environment.json"

        with open(env_Path, "r") as env:
            read_file = json.load(env)
            self.configInfo.update(read_file)
            item = self.configInfo['PaperTrail'].get(param)
            return item
