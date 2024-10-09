from automation_Pages.DashboadPage import DashBoard


class AssetAllocation(DashBoard):

    def __init__(self, driver):
        super().__init__(driver)

    def deleteAllocationCases(self):
        path = "i[data-action='Delete']"
        count = self.selenide.getElementCount("css", path)
        if count > 1:
            for e in range(count):
                self.selenide.clickElement("css", path)
                self.actionOnDeletePopUp("Ok")
        self.log.info("Deleted all existing Allocation Cases")

    def clickAddAssumptionSetIcon(self):
        self.selenide.clickElement("css", "a[title='Add Assumption Set']")
        self.log.info("Clicked on Add Assumption Set")
        self.selenide.waitTime(1)

    def clickAddAllocationCaseIcon(self):
        self.selenide.clickElement("css", "i[title='Add Allocation Case']")
        self.log.info("Clicked on Add Allocation Case")
        self.selenide.waitTime(1)

    def enterAllocationCaseName(self, caseName):
        self.selenide.enterText("css", "input[value='New Case']", caseName)
        self.log.info("Entered an Assumption Set Name")

    def selectAssumptionSets(self):
        self.selenide.clickElement("css", "select[class='form-control']")

    def openNewAssumptionSet(self):
        self.selenide.clickElement("xpath", "(//span[text()]) [last()]")
        self.log.info("Clicked on newly created Assumption Set")

    def VerifyColumnHeader(self, labels):
        self.selenide.verifyVisible("xpath", str.format("//div[contains(@id, 'slickgrid')]/span[text()='{0}']", labels))
        self.log.info("Verifying Column Header", labels)
