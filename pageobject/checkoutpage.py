from selenium.webdriver.common.by import By

from pageobject.confirmpage import confirmpage


class checkoutpage:
    def __init__(self,driver):
        self.driver = driver

    #driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    getcard =(By.XPATH, "//div[@class='card h-100']")

    def titles (self):
        return self.driver.find_elements(*checkoutpage.getcard)

    #(By.XPATH, "//a[@class='nav-link btn btn-primary']")
    checkoutbutts = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    def getbutts(self):
        return self.driver.find_element(*checkoutpage.checkoutbutts)

    #(By.CSS_SELECTOR, ".btn.btn-success")
    success = (By.CSS_SELECTOR, ".btn.btn-success")

    def getsuccess(self):
        self.driver.find_element(*checkoutpage.success).click()
        confirmpages = confirmpage(self.driver)
        return confirmpages
