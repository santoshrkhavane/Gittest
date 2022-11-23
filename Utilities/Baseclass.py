import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.usefixtures("setup")
class Baseclass:
    def verifyLinkPresance(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,text)))

    def selectoptionBytext(self,locator,text):
        sc = Select(locator)
        sc.select_by_visible_text(text)