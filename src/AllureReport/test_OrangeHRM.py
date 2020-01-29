'''
Created on 27-Jan-2020

@author: praveen
'''
from selenium import webdriver
import allure
import pytest
from allure_commons.types import AttachmentType

@allure.severity(allure.severity_level.NORMAL)
class TestOrangeHRM:
    @allure.severity(allure.severity_level.MINOR)
    def test_Logo(self):
        self.driver = webdriver.Chrome(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver")
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        logo1 = self.driver.find_element_by_xpath("//*[@id='divLogo']/img")
        if logo1.is_displayed():
            self.driver.close()
            assert True
        else :
            allure.attach(self.driver.get_screenshot_as_png(),name="test logo screen",
                          attachment_type = AttachmentType.PNG)
            self.driver.close()
            assert False
        
            
    @allure.severity(allure.severity_level.NORMAL)
    def test_listemployees(self):
        pytest.skip("Skipping test...Later I will implement ")
        
    @allure.severity(allure.severity_level.CRITICAL)    
    def test_Login(self):
        self.driver = webdriver.Chrome(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver")
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        usr = self.driver.find_element_by_id("txtUsername")
        pwd = self.driver.find_element_by_id("txtPassword")
        lg_bttn = self.driver.find_element_by_id("btnLogin")
        
        usr.send_keys("admin")
        pwd.send_keys("admin")
        lg_bttn.click()
        
        tit2 = self.driver.title
        
        if tit2 == "OrangeHRM113":
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="test login screen",
                          attachment_type = AttachmentType.PNG)
            self.driver.close()
            assert False
            
            
        
        
        