from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pages.login_page import LoginPage
from utils.datos import leer_csv_login  

#a parte del parametro usuario y contraseña le paso el parametro que diga si la prueba debe pasar o no
#tambien le paso la funcion que lee los datos del archivo datos
@pytest.mark.parametrize("usuario, password, debe_funcionar",leer_csv_login("datos/data_login.csv"))
def test_login_validation(login_in_driver, usuario, password, debe_funcionar):#le pasamos la funcion login_in_driver
    try:
        driver = login_in_driver#todo lo que me devuelve la funcion login la pongo en una variables driver ya que la vamos a utilizar nuevamente

        if (debe_funcionar) == 'True':
            #Validacion de la redireccion de la pagina
            assert "/inventory.html" in driver.current_url, "No se redirigio correctamente al inventario"#comparo la lo que metrajo la funcion login_in_driver con la url si no coiciden doy un mensaje de No se dirigio la pagina 
        elif (debe_funcionar) == 'False':
            mensaje_error = LoginPage(driver).obtener_error()#estoy evaluando si existe el mensaje de error
            assert "Epic sadface" in mensaje_error, "el mensaje de error no se esta mostrando"
        #despues para cada mensaje de error deberia hacer un if diferente

    except Exception as e:#manejo de errores en el login
        print(f"Error en test_login: {e}")
        raise #se finaliza la prueba a traves del error 
    finally:
        driver.quit()

    
