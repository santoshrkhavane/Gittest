from selenium.webdriver.common.by import By
class confirmpage:
    def __init__(self,driver):
        self.driver = driver

    country =(By.ID, "country")
    DrpOpt =(By.LINK_TEXT, "India")
    Chck =(By.XPATH, "//label[@for='checkbox2']")
    Sub =(By.XPATH, "//input[@type='submit']")
    SuccMsg =(By.CSS_SELECTOR, ".alert")

    def getcountry(self):
        return self.driver.find_element(*confirmpage.country)

    def getDrpOpt(self):
        return self.driver.find_element(*confirmpage.DrpOpt)

    def getChck(self):
        return self.driver.find_element(*confirmpage.Chck)

    def getSub(self):
        return self.driver.find_element(*confirmpage.Sub)

    def getSuccMsg(self):
        return self.driver.find_element(*confirmpage.SuccMsg)







