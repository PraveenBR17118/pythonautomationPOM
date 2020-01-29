'''
Created on 27-Jan-2020

@author: praveen
'''
from selenium import webdriver
import pytest

class TestOrangeHRM():
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver")
        self.driver.maximize_window()
        yield 
        self.driver.close()
        
    def test_homePageTitle(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        tit1 = self.driver.title
        assert tit1 == "OrangeHRM123"
        
        
    def test_login(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        usr = self.driver.find_element_by_id("txtUsername")
        pwd = self.driver.find_element_by_id("txtPassword")
        lg_bttn = self.driver.find_element_by_id("btnLogin")
        
        usr.send_keys("admin")
        pwd.send_keys("admin")
        lg_bttn.click()
        tit2 = self.driver.title
        assert tit2 == "OrangeHRM"