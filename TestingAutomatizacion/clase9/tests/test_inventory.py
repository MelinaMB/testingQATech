from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

@pytest.mark.parametrize("usuario, password",[("standard_user","secret_sauce")])
def test_inventory(login_in_driver,usuario,password):
    
    try:
        driver = login_in_driver
        LoginPage(driver).login_completo(usuario,password)
        inventory_page = InventoryPage(driver) #instancio la clase InventoryPage, paso la variable driver para hacer el link entre el driver y las funciones que estan en inventory_page
        
        #verifico que hay productos
        assert len(inventory_page.obtener_todos_los_productos()) > 0, "El inventario esta vacio"

        #verificar que el carrito este vacio al inicio
        assert inventory_page.obtener_conteo_carrito() == 0

        #Agregar el primer producto
        inventory_page.agregar_primer_producto()

        #Verificar que el contador del carrito sea igual a 1
        assert inventory_page.obtener_conteo_carrito() == 1
    
    except Exception as e:
        print(f"Error en test_invetory: {e}")
        raise
        
    finally:
        driver.quit()