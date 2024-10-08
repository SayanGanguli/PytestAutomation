import yaml
from pathlib import Path
import string
import random
from random import randint


def readConfig():
    app_details = {}
    path = Path(__file__).parent / "environment.yaml"
    with open(path, 'r') as f:
        files = list(yaml.load_all(f, Loader=yaml.FullLoader))
        for i in files:
            app_details.update(i)
        return app_details


def getRegionValues(country, field):
    region_details = {}
    credentials = {}
    for i in readConfig().get("Region"):
        region_details.update(i)

    for j in region_details.get(country):
        credentials.update(j)
    return credentials.get(field.lower())


def getOCCValues(console, field):
    occ_details = {}
    credentials = {}
    for i in readConfig().get("OCC"):
        occ_details.update(i)

    for j in occ_details.get(console):
        credentials.update(j)
    return credentials.get(field.lower())


def getEmailValues(field):
    credentials = {}
    for i in readConfig().get("Email"):
        credentials.update(i)
    return credentials.get(field.lower())


def generateRandomString():
    res = ''.join(random.choices(string.ascii_lowercase +
                                 string.digits, k=3))
    return res


def generateRandomNumber():
    num = randint(10, 999999)
    return str(num)


def generateRandomMail():
    res = generateRandomString()
    mail_format = "auto_test{0}@yopmail.com".format(res)
    return mail_format


#region = "Finland"
region = "Norway"
#region = "Europe"
#region = "France"
#region = "Denmark"
#region = "Poland"
#region = "Germany"

new_mail = generateRandomMail()
url = getRegionValues(region, "url")
uname = getRegionValues(region, "username")
pwd = getRegionValues(region, "password")

account_name = getOCCValues("Account", "Name")
admin_url = getOCCValues("Admin", "URL")
agent_url = getOCCValues("Agent", "URL")
occ_uname = getOCCValues("Admin", "Username")
occ_pwd = getOCCValues("Agent", "Password")
emailId = getEmailValues("Mail")
email_link = getEmailValues("URL")
dummy_mail = "automation_tester@yopmail.com"
