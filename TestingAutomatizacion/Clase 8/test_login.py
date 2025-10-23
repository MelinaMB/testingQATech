from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By

def test_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5) # es dinamico te hace esperar como maximo 5 segundos entre cada accion y accion


    try:
    # login
        driver.get("https://www.saucedemo.com/")
        
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        

    #Validacion de la redireccion de la pagina

        assert '/inventory.html' in driver.current_url, "No se redirigio correctamente al inventario"

        print("TEST OK")

    except Exception as e:
        print(f"Error en test_login: {e}")
        raise #se finaliza la prueba a traves del error 