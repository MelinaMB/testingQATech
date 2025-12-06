from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_carrito(login_in_driver):
    
    try:
        driver = login_in_driver
        #interacciones

        productos = driver.find_elements(By.CLASS_NAME,"inventory_item")
        productos[0].find_element(By.TAG_NAME, "button").click()

        carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert carrito == "1", "El carrito no se actualizo correctamente"

        driver.find_element(By.CLASS_NAME, "shopping-cart-link").click()
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        nombre_invetory = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
        nombre_cart = cart_items[0].find_element(By.CLASS_NAME, "inventory_item_name").text
        assert nombre_invetory == nombre_cart, "El producto en el carrito no coincide"

    finally:
        driver.quit()