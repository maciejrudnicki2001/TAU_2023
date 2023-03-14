from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)


def test_succesfful_login():
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    
    if ("https://www.saucedemo.com/inventory.html" == driver.current_url):

        print("\033[92m" + "Test 1/8 Passed" + "\033[0m")
    else:

        print("\033[91m" + "Test 1/8 Failed" + "\033[0m")

def test_locked_out_user():
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    if ("Epic sadface: Sorry, this user has been locked out." == error_message.text):

        print("\033[92m" + "Test 2/8 Passed" + "\033[0m")
    else:

        print("\033[91m" + "Test 2/8 Failed" + "\033[0m")

def test_invalid_username():
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    if ("Epic sadface: Username and password do not match any user in this service" == error_message.text):

        print("\033[92m" + "Test 3/8 Passed" + "\033[0m")
    else:

        print("\033[91m" + "Test 3/8 Failed" + "\033[0m")

def test_invalid_password():
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("invalid_password")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    if ("Epic sadface: Username and password do not match any user in this service" == error_message.text):

        print("\033[92m" + "Test 4/8 Passed" + "\033[0m")
    else:

        print("\033[91m" + "Test 4/8 Failed" + "\033[0m")

def test_empty_username():
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    if ("Epic sadface: Username is required" == error_message.text):

        print("\033[92m" + "Test 5/8 Passed" + "\033[0m")
    else:

        print("\033[91m" + "Test 5/8 Failed" + "\033[0m")

def test_empty_password():
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    if ("Epic sadface: Password is required" == error_message.text):

        print("\033[92m" + "Test 6/8 Passed" + "\033[0m")
    else:

        print("\033[91m" + "Test 6/8 Failed" + "\033[0m")

def test_empty_username_and_password():
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("")
    driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    if ("Epic sadface: Username is required" == error_message.text):

        print("\033[92m" + "Test 7/8 Passed" + "\033[0m")
    else:

        print("\033[91m" + "Test 7/8 Failed" + "\033[0m")

def test_login_with_special_characters():
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_$sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    if ("Epic sadface: Username and password do not match any user in this service" == error_message.text):

        print("\033[92m" + "Test 8/8 Passed" + "\033[0m")
    else:

        print("\033[91m" + "Test 8/8 Failed" + "\033[0m")

def teardown_module():
    driver.quit()


test_succesfful_login()
test_locked_out_user()
test_invalid_username()
test_invalid_password()
test_empty_username()
test_empty_password()
test_empty_username_and_password()
test_login_with_special_characters()
teardown_module()

