from selenium.webdriver.common.by import By
from pageobject.checkoutpage import checkoutpage
class homepage:
    def __init__(self,driver):
        self.driver = driver

    #driver.find_element(By.XPATH, "//a[text()='Shop']")
    shop =(By.XPATH, "//a[text()='Shop']")

    #driver.find_element(By.CSS_SELECTOR, "input[@name='name']")
    name =(By.CSS_SELECTOR, "input[name='name']")

    #driver.find_element(By.NAME, "email")
    email = (By.NAME,"email")

    #driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1"))
    drpdwn = (By.CSS_SELECTOR, "#exampleFormControlSelect1")

    #driver.find_element(By.XPATH, "//input[@value='Submit']")
    sub = (By.XPATH, "//input[@value='Submit']")

    #driver.find_element(By.XPATH, "//form-comp/div/div[2]/div")
    Msg = (By.XPATH, "//form-comp/div/div[2]/div")

    def shopitems(self):
        self.driver.find_element(*homepage.shop).click()
        Checkoutpage = checkoutpage(self.driver)
        return Checkoutpage

    def getname(self):
        return self.driver.find_element(*homepage.name)

    def getemail(self):
        return self.driver.find_element(*homepage.email)

    def getdrp(self):
        return self.driver.find_element(*homepage. drpdwn)

    def submit(self):
        return self.driver.find_element(*homepage.sub)

    def massg(self):
        return self.driver.find_element(*homepage.Msg)

