from automation_Engine import selenide
from automation_Pages.DashboadPage import DashBoard


class CreatePortfolio(DashBoard):
    def __init__(self, driver):
        super().__init__(driver)

    """
    CleanUpPortfolio method deletes all the existing portfolio from the grid
    """
    def cleanUpPortfolio(self):
        self.selenide.clickElement("css","label[class='checkbox-line'] label")
        portfolioNames = self.selenide.getElementList("xpath","//div[@class='grid-canvas']/div/div[1]")
        for name in portfolioNames:
            if not name.__contains__("Do") \
                    or name.__contains__("Aug") or name.__contains__("Jan") or name.__contains__("Oct"):
                self.deletePortfolio(name)













