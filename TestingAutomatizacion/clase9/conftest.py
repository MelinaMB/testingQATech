# el archivo conftest permite compartir configuraciones de forma global
#no es un archivo de prueba, sirve para centralizar la informacion que pueda requerir los test en general
#debe estar siempre en la raiz del proyecto para que pytest lo detecte automaticamente   
#se utiliza cuando tengo especificaciones ue se usan en varios test como por ejemplo conectarme en una base de datos, preparar datos de prueba, hacer el login
#son cosas primordiales que se repiten en la gran mayoria de las pruebas
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from datetime import datetime
import time
#variable que me genera la carpeta donde se va a guardar las capturas de pantalla
import pathlib
target = pathlib.Path("reports/screens")
target.mkdir(parents=True, exist_ok=True) 

#defino las funciones que voy a reutilizar en mis test
@pytest.fixture
def driver():
    chrome_opt = Options() #abre chrome como incognito y desactiva popup de contraseña filtrada 
    chrome_opt.add_argument("--incognito")
    driver = webdriver.Chrome(options = chrome_opt)#guardo en una variable el inicializador del navegador con el que voy a trabajar
    yield driver # se utiliza para los fixture en pytest para devolver un valor al test
                 # despues de que el test termina continua ejecutando el test que viene
    driver.quit()#funcion para cerrar el navegador 

###
#@pytest.fixture
#def login_in_driver(driver):#se esta globalizando la funcion de login_in_driver
#    login(driver)
#    return driver
###

#yield y return ambos devuelven
#el return devuelve un valor 
#el yield pausa la funcion para poder ejecutar la prueba en el medio, nos da la posibilidad de meter la logica de mi pagina y poder hacer la prueba

#globalizo la funcion de login
@pytest.fixture
def login_in_driver(driver):
    LoginPage(driver).abrir_pagina()
    return driver
#aca deberia hacer otro conftest para login invalido con su mensaje de error

#--------------------------------------------------------------------------

@pytest.fixture
def url_base():
    return "https://reqres.in/api/users"

@pytest.fixture
def header_request():
    return {"x-api-key": "reqres_be64950124cf4da780382775b0a9adcb"}

@pytest.hookimpl(hookwrapper=True)#ejecuta el codigo el test y luego el hook dentro del test
def pytest_runtest_makereport(item,call):#item los nombre del test y los fixture y call las instrucciones para hacer las tomas de captura
    outcome = yield #especie de return en vez de devolver un valor pausa la funcion y lo guarda, la proxima vez que la funcion se reanude sigue donde se quedo
    report = outcome.get_result()

    #estoy diciendo si el test fallo antes de empezar o fallo durante el test saco captura de pantalla y cuando falla es decir cuando el test fallo
    if report.when in ("setup","call") and report.failed: #setup y call son fases del ciclo de la ejecucion de la prueba en tres etapas, setup es la preparacion del test definimos y creamos los fixtures, inicializamos el drive, selenium , call es la ejecucion del test y tesrdawn(ver si se escribe asi) es la limpieza del test
        driver = item.funcargs.get("driver",None)#funcargs es el fixture

        if driver:#defino esl archivo(la imagen) que se va a generar y que se va a guardar
            timestamp_comun = datetime.now().strftime("%Y%m%d_%H%M%S")
            timestamp_unix = int(time.time())
            file_name = target / f"{report.when}_{item.name}_{timestamp_comun}.png"
            driver.save_screenshot(str(file_name))