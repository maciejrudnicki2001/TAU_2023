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


def test_check_item_in_cart(x):
    # Przejście do koszyka
    cart_button = driver.find_element(By.ID, "shopping_cart_container")
    cart_button.click()
    time.sleep(2)





def order_item(x):
    # Przejście do podsumowania zamówienia
    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()
    time.sleep(2)

    # Wypełnienie formularza
    driver.find_element(By.ID, "first-name").send_keys("Jan")
    driver.find_element(By.ID, "last-name").send_keys("Kowalski")
    driver.find_element(By.ID, "postal-code").send_keys("00-000")
    time.sleep(2)

    # Przejście do podsumowania zamówienia
    checkout_button = driver.find_element(By.ID, "continue")
    checkout_button.click()
    time.sleep(2)

    # Potwierdzenie zamówienia
    finish_button = driver.find_element(By.ID, "finish")
    finish_button.click()
    time.sleep(2)

    # Sprawdzenie czy zamówienie zostało złożone
    if ("https://www.saucedemo.com/checkout-complete.html" == driver.current_url and x == 0):
        print("Test passed order completed")



test_open_saucedemo(0)
test_login(0)
test_add_item(0)
test_check_item_in_cart(0)
order_item(0)