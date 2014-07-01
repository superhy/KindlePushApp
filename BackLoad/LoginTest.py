'''
Created on 2013-2-8

@author: Administrator
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Untitled(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.renren.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("superhy199148@gmail.com")  #username
        driver.find_element_by_id("pwdTip").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("232323")   #password
        driver.find_element_by_id("login").click()
        driver.find_element_by_css_selector("#showFriendMenu > span.menu-title-text").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert.text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
       

if __name__ == "__main__":
    unittest.main()
