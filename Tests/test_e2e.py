from selenium.webdriver.common.by import By
from Utilities.Baseclass import Baseclass
from pageobject.homepage import homepage

class TestOne(Baseclass):
    def test_e2e(self):
        #self.driver.find_element(By.XPATH, "//a[text()='Shop']").click()
        Homepage = homepage(self.driver)
        self.driver.implicitly_wait(5)

        Checkoutpage = Homepage.shopitems()
        #list = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        #chekoutpage = checkoutpage(self.driver)
        products = Checkoutpage.titles()
        for product in products:
            if product.find_element(By.XPATH, "div/h4/a").text == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()
                break
        #self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        Checkoutpage.getbutts().click()

        #self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()
        confirmpages = Checkoutpage.getsuccess()

        #self.driver.find_element(By.ID, "country").send_keys("Ind")
        confirmpages.getcountry().send_keys("Ind")
        #self.time.sleep(8)

        # Expicit Wait
        self.verifyLinkPresance("India")

        #self.driver.find_element(By.LINK_TEXT, "India").click()
        confirmpages.getDrpOpt().click()

        #self.driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
        confirmpages.getChck().click()

        #self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        confirmpages.getSub().click()

        #sms = self.driver.find_element(By.CSS_SELECTOR, ".alert").text
        successMsg = confirmpages.getSuccMsg().text
        assert "Success! Thank you!" in successMsg


