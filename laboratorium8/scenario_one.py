from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)


def test_open_saucedemo(x):
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

def test_login(x):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    if ("https://www.saucedemo.com/inventory.html" == driver.current_url and x == 0):
        print("Test passed you are logged in")

test_open_saucedemo(0)
test_login(0)