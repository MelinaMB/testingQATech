from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_carrito(login_in_driver):
    
    try:
        driver = login_in_driver
        
       # traigo todos los elementos del catalogo
        productos = driver.find_elements(By.CLASS_NAME,"inventory_item")
        #hago click en el boton agregar al carrito
        productos[0].find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        # obtengo el nombre del primer producto del catalogo
        nombre_invetory = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
        time.sleep(5)

        #corroboro que el icono de carrito se puso en 1 luego de agregar un producto al carrito
        carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert carrito == "1", "El carrito no se actualizo correctamente"

        #hago click en el carrito para ir al carrito
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(3)
        #obtengo el iten del carrito
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        #obtengo el nombre del item del carrito
        nombre_cart = cart_items[0].find_element(By.CLASS_NAME, "inventory_item_name").text
        #comparo que el item del carrito sea el mismo que agregue al carrito
        assert nombre_invetory == nombre_cart, "El producto en el carrito no coincide"

        
    finally:
        driver.quit()