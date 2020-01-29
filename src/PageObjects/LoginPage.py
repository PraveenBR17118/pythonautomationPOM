'''
Created on 23-Jan-2020

@author: praveen
'''
class LoginPage():
#identify all the locators of the page
    usr_name_id  = "Email" 
    pwd_id = "Password"
    lgn_bttn_xpath = "//input[@type='submit']"
    lgout_bttn_xpath = "//a[@href='/logout']"
    
    #admin@yourstore.com
    #admin
    
    def __init__(self,driver):
        self.driver = driver
        
    def setUserName(self,username):
        self.driver.find_element_by_id(self.usr_name_id).send_keys(username)
        
    def setPassword(self,password):
        self.driver.find_element_by_id(self.pwd_id).send_keys(password)
        
    def clickLogin(self):
        self.driver.find_element_by_xpath(self.lgn_bttn_xpath).click()
        
    def clickLogout(self):
        self.driver.find_element_by_xpath(self.lgout_bttn_xpath).click()