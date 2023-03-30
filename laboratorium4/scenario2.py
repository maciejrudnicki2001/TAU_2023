import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestScenario2(unittest.TestCase):


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
        self.username = self.driver.find_element(By.ID, "user-name")
        self.password = self.driver.find_element(By.ID, "password")
        self.login = self.driver.find_element(By.ID, "login-button")

    def test_login(self):
        self.username.send_keys("standard_user")
        self.password.send_keys("secret_sauce")
        self.login.click()
        self.assertEqual("https://www.saucedemo.com/inventory.html", self.driver.current_url)

    def test_locked_out_user(self):
        self.username.send_keys("locked_out_user")
        self.password.send_keys("secret_sauce")
        self.login.click()
        error_message = self.driver.find_element(By.XPATH, "//h3[@data-test='error']")
        self.assertEqual("Epic sadface: Sorry, this user has been locked out.", error_message.text)

    def test_invalid_username(self):
        self.username.send_keys("invalid_user")
        self.password.send_keys("secret_sauce")
        self.login.click()
        error_message = self.driver.find_element(By.XPATH, "//h3[@data-test='error']")
        self.assertEqual("Epic sadface: Username and password do not match any user in this service", error_message.text)

    def test_invalid_password(self):
        self.username.send_keys("standard_user")
        self.password.send_keys("invalid_password")
        self.login.click()
        error_message = self.driver.find_element(By.XPATH, "//h3[@data-test='error']")
        self.assertEqual("Epic sadface: Username and password do not match any user in this service", error_message.text)

    def test_empty_username(self):
        self.username.send_keys("")
        self.password.send_keys("secret_sauce")
        self.login.click()
        error_message = self.driver.find_element(By.XPATH, "//h3[@data-test='error']")
        self.assertEqual("Epic sadface: Username is required", error_message.text)

    def test_empty_password(self):
        self.username.send_keys("standard_user")
        self.password.send_keys("")
        self.login.click()
        error_message = self.driver.find_element(By.XPATH, "//h3[@data-test='error']")
        self.assertEqual("Epic sadface: Password is required", error_message.text)

    def test_empty_username_and_password(self):
        self.username.send_keys("")
        self.password.send_keys("")
        self.login.click()
        error_message = self.driver.find_element(By.XPATH, "//h3[@data-test='error']")
        self.assertEqual("Epic sadface: Username is required", error_message.text)

    def test_login_with_special_characters(self):
        self.username.send_keys("standard_user")
        self.password.send_keys("secret_$auce")
        self.login.click()
        error_message = self.driver.find_element(By.XPATH, "//h3[@data-test='error']")
        self.assertEqual("Epic sadface: Username and password do not match any user in this service", error_message.text)
 
    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()