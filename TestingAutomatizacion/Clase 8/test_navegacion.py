from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def test_navegacion():
    driver = webdriver.Chrome() #especificamos que navegador vamos a utilizar
    driver.implicitly_wait(5)

    try:
        driver.get("https://www.saucedemo.com/") #ingreso a la pagina que quiero hacer las pruebas
        print("Titulo:",driver.title)
        assert driver.title == "Swag Labs" # comparo el titulo de la pagina con el que yo espero que tenga
        time.sleep(2) #dejar un tiempo para poder ver todo lo que ocurre

        print("TEST OK")
        
    finally:
        driver.quit() # no se utiliza si estoy haciendo test en formato modulo, es decir que despues 
                      # de esta prueba va otra y si yo pongo quit se va a cerrar el web driver  y ya no voy a poder seguir
         