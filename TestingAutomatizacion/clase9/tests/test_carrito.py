from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.mark.parametrize("usuario, password",[("standard_user","secret_sauce")])
def test_carrito(login_in_driver,usuario,password):
    
    try:
        driver = login_in_driver
        LoginPage(driver).login_completo(usuario,password)
        cart_page = CartPage(driver)
        inventory_page = InventoryPage(driver)

        #Agregar al carrito el producto
        inventory_page.agregar_primer_producto()

        #Abrir el carrito
        inventory_page.abrir_carrito()

        #Validar el producto
        productos_en_carrito = cart_page.obtener_productos_carrito()
        assert len(productos_en_carrito) == 1
        #forsar un fallo en una prueba
        #assert False, "Fallo de prueba forsado"

    except Exception as e:
        print(f"Error en test_cart: {e}")
        raise
        
    #finally:
        #driver.quit()