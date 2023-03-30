import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestScenario3(unittest.TestCase):
    
    browser = ''

    def setUpBrowser(self, browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'edge':
            self.driver = webdriver.Edge()
        elif browser == 'opera':
            self.driver = webdriver.Opera()
        else:
            raise Exception("Invalid browser name")
        
        return self.driver
    
    def setUp(self):
        self.driver = self.setUpBrowser('edge')
        self.driver.get("https://www.saucedemo.com/")
        self.username = self.driver.find_element(By.ID, "user-name")
        self.password = self.driver.find_element(By.ID, "password")
        self.login = self.driver.find_element(By.ID, "login-button")

    def test_additional_feature(self):
        
        self.username.send_keys("standard_user")
        self.username.send_keys("secret_sauce")
        self.login.click()
        self.assertIn("Swag Labs", self.driver.title)


if __name__ == '__main__':
    unittest.main()
    