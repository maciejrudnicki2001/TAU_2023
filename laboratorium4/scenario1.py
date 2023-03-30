import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestScenario1(unittest.TestCase):

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
        self.driver = self.setUpBrowser(self.browser)
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.logo = self.driver.find_element(By.CLASS_NAME, "login_logo")
        self.footer = self.driver.find_element(By.CLASS_NAME, "login_credentials_wrap")

    def test_open_saucedemo(self):
        self.assertEqual("https://www.saucedemo.com/", self.driver.current_url)
        self.assertTrue(self.logo.is_displayed())
        self.assertTrue(self.footer.is_displayed())

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()