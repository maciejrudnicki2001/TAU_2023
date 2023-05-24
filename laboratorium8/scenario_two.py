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


def test_add_item(x):
    # Wybór produktu i dodanie do koszyka
    product = driver.find_element(By.ID, "item_4_title_link")
    product.click()

    add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_to_cart_button.click()
    time.sleep(2)

    # Jeśli przy ikonie koszyka jest liczba 1 to znaczy, że produkt został dodany do koszyka
    if (driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text == "1"):
        print("Test passed item added to cart")



test_open_saucedemo(0)
test_login(0)
test_add_item(0)