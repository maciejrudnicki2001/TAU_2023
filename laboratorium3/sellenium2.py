from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

def test_open_saucedemo(x):
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    if ("https://www.saucedemo.com/" == driver.current_url and x == 0):
        print("\033[92m" + "Test 1/10 Passed" + "\033[0m")
    elif (x == 0):
        print("\033[91m" + "Test 1/10 Failed" + "\033[0m")

def test_login(x):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    if ("https://www.saucedemo.com/inventory.html" == driver.current_url and x == 0):
        print("\033[92m" + "Test 2/10 Passed" + "\033[0m")
    elif (x == 0):
        print("\033[91m" + "Test 2/10 Failed" + "\033[0m")

def test_locked_out_user():
    test_open_saucedemo(1)
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    if ("Epic sadface: Sorry, this user has been locked out." == error_message.text):

        print("\033[92m" + "Test 3/10 Passed" + "\033[0m")
    else:

        print("\033[91m" + "Test 3/10 Failed" + "\033[0m")

def test_invalid_username():
    test_open_saucedemo(1)
    driver.find_element(By.ID, "user-name").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    if ("Epic sadface: Username and password do not match any user in this service" == error_message.text):

        print("\033[92m" + "Test 4/10 Passed" + "\033[0m")
    else:

        print("\033[91m" + "Test 4/10 Failed" + "\033[0m")

def test_invalid_password():
    test_open_saucedemo(1)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("invalid_password")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    if ("Epic sadface: Username and password do not match any user in this service" == error_message.text):

        print("\033[92m" + "Test 5/10 Passed" + "\033[0m")
    else:
        print("\033[91m" + "Test 5/10 Failed" + "\033[0m")

def test_empty_username():
    test_open_saucedemo(1)
    driver.find_element(By.ID, "user-name").send_keys("")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    if ("Epic sadface: Username is required" == error_message.text):

        print("\033[92m" + "Test 6/10 Passed" + "\033[0m")
    else:

        print("\033[91m" + "Test 6/10 Failed" + "\033[0m")

def test_empty_password():
    test_open_saucedemo(1)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    if ("Epic sadface: Password is required" == error_message.text):

        print("\033[92m" + "Test 7/10 Passed" + "\033[0m")
    else:
        print("\033[91m" + "Test 7/10 Failed" + "\033[0m")

def test_empty_username_and_password():
    test_open_saucedemo(1)
    driver.find_element(By.ID, "user-name").send_keys("")
    driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    if ("Epic sadface: Username is required" == error_message.text):

        print("\033[92m" + "Test 8/10 Passed" + "\033[0m")
    else:

        print("\033[91m" + "Test 8/10 Failed" + "\033[0m")

def test_login_with_special_characters():
    test_open_saucedemo(1)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_$sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)

    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    if ("Epic sadface: Username and password do not match any user in this service" == error_message.text):
        print("\033[92m" + "Test 9/10 Passed" + "\033[0m")
    else:
        print("\033[91m" + "Test 9/10 Failed" + "\033[0m")

def test_additional_feature():
    test_open_saucedemo(1)
    test_login(1)
    assert "Swag Labs" in driver.title
    if ("Swag Labs" in driver.title):
        print("\033[92m" + "Test 10/10 Passed" + "\033[0m")
    else:
        print("\033[91m" + "Test 10/10 Failed" + "\033[0m")
    
    driver.quit()

    
test_open_saucedemo(0)
test_login(0)
test_locked_out_user()
test_invalid_username()
test_invalid_password()
test_empty_username()
test_empty_password()
test_empty_username_and_password()
test_login_with_special_characters()
test_additional_feature()