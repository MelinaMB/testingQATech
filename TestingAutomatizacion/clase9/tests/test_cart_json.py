from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from utils.lector_json import leer_json_productos
from pages.login_page import LoginPage
RUTA_JSON = "datos/productos.json"

@pytest.mark.parametrize("usuario, password",[("standard_user","secret_sauce")])
@pytest.mark.parametrize("nombre_producto", leer_json_productos(RUTA_JSON))
def test_cart_json(login_in_driver,usuario,password,nombre_producto):
    
    try:
        driver = login_in_driver
        LoginPage(driver).login_completo(usuario,password)
        cart_page = CartPage(driver)
        inventory_page = InventoryPage(driver)

        #Agregar al carrito el producto
        inventory_page.agrgar_producto_por_nombre(nombre_producto)

        #Abrir el carrito
        inventory_page.abrir_carrito()
        time.sleep(2)

        #Validar el producto
        productos_en_carrito = cart_page.obtener_nombre_producto_carrito()
        assert len(productos_en_carrito) == 1

    except Exception as e:
        print(f"Error en test_cart: {e}")
        raise
        
    finally:
        driver.quit()