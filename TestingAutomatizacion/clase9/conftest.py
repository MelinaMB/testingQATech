# el archivo conftest permite compartir configuraciones de forma global
#no es un archivo de prueba, sirve para centralizar la informacion que pueda requerir los test en general
#debe estar siempre en la raiz del proyecto para que pytest lo detecte automaticamente   
#se utiliza cuando tengo especificaciones ue se usan en varios test como por ejemplo conectarme en una base de datos, preparar datos de prueba, hacer el login
#son cosas primordiales que se repiten en la gran mayoria de las pruebas
import pytest
from selenium import webdriver
from utils import login
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage

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

#globalizo la fincion de login
@pytest.fixture
def login_in_driver(driver, usuario, password):
    LoginPage(driver).abrir_pagina().login_completo(usuario, password)
    return driver

#aca deberia hacer otro conftest para login invalido con su mensaje de error