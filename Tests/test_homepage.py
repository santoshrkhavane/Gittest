import pytest
from Test_data.Homepage_data import Homepagedata
from Utilities.Baseclass import Baseclass
from pageobject.homepage import homepage


class TesthomePage(Baseclass):
    @pytest.fixture(params=Homepagedata.test_data_homepage)
    def getdata(self,request):
        return request.param
    def test_formsumbtion(self,getdata):

        Homepages = homepage(self.driver)
        # driver.find_element(By.NAME,"name").send_keys("Santosh")
        Homepages.getname().send_keys(getdata["firstname"])

        #self.driver.find_element(By.NAME,"email").send_keys("santosh.khavane@cogniwise.com")
        Homepages.getemail().send_keys(getdata["email"])
        self.selectoptionBytext(Homepages.getdrp(), getdata["gender"])

        #self.driver.find_element(By.XPATH,"//input[@value='Submit']").click()
        Homepages.submit().click()

        sms = Homepages.massg().text
        assert "Success" in sms

