#utils la funcion logica de como accedo a mi pagina, como interactuo con la pagina y como obtengo los valores de la pagina
import time
from selenium.webdriver.common.by import By

def login(driver): # creo un parametro que es driver con el que yo voy a hacer referencia al navegador que estoy evaluando
                   # en el archivo conftest esta la configuracion para driver
    #voy a la pagina que quiero testear
    driver.get("https://www.saucedemo.com/")

    #mando las credenciales para hacer el login
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    time.sleep(2)
        