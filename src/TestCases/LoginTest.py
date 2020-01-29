'''
Created on 23-Jan-2020

@author: praveen
'''
from PageObjects.LoginPage import LoginPage
import unittest
import HtmlTestRunner
import time
#import sys
from selenium import webdriver
#sys.path.append("/Users/praveen/Documents/Eclipse Project/PythonAutomation/PythonUnitTestProject_POMBased/POM")

class LoginTest(unittest.TestCase):
    baseUrl = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Chrome(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/PythonUnitTestProject_POMBased/POM/Drivers/chromedriver")
    
    @classmethod
    def setUpClass(cls):
        #cls.driver = webdriver.Chrome(executable_path="/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/Drivers/chromedriver")
        cls.driver.get(cls.baseUrl)
        cls.driver.maximize_window()
        
    def test_Login(self):
        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        tit1 = self.driver.title
        
        time.sleep(5)
        
        self.assertEqual("Dashboard / nopCommerce administration",tit1,"Title is different")
        
    @classmethod 
    def tearDownClass(cls):
        cls.driver.close()
        print("Test Completed.......")
        
if __name__ == "__main__":
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output = "/Users/praveen/Documents/Eclipse Project/PythonAutomation/PythonUnitTestProject_POMBased/POM/Reports"))
        
    
    