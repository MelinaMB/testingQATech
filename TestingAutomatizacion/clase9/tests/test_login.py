from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_validation(login_in_driver):#le pasamos la funcion login_in_driver
    try:
        driver = login_in_driver#todo lo que me devuelve la funcion login la pongo en una variables driver ya que la vamos a utilizar nuevamente

        #Validacion de la redireccion de la pagina
        assert "/inventory.html" in driver.current_url, "No se redirigio correctamente al inventario"#comparo la lo que metrajo la funcion login_in_driver con la url si no coiciden doy un mensaje de No se dirigio la pagina 


    except Exception as e:#manejo de errores en el login
        print(f"Error en test_login: {e}")
        raise #se finaliza la prueba a traves del error 
    finally:
        driver.quit()

    
