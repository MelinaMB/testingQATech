from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_navegacion(login_in_driver):
    

    try:
        driver = login_in_driver

        # comparo el titulo de la pagina con el que yo espero que tenga
        assert driver.title == "Swag Labs" 

        #obtengo los items del catalogo
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        #verifico que existe al menos un producto en el catalogo
        assert len(products) > 0, "No hay productos visibles en la pagina"

        #verifico que hay un menu
        driver.find_element(By.ID, "react-burger-menu-btn").click()

        #verifico que hay un filtro y que pueda filtrar
        filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
        time.sleep(3)
        opcion = Select(filtro)
        #filtro de A to Z
        opcion.select_by_value("az")
        #filtro de precio low to high
        opcion.select_by_value("lohi")
        time.sleep(3)
        
    except Exception as e:
        print(f"Error en test_navegacion: {e}")
        raise #se finaliza la prueba a traves del error 
    finally:
        driver.quit() 
         

