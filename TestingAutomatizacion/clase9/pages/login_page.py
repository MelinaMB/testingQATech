#
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait #importa la espera
from selenium.webdriver.support import expected_conditions as EC #importa las condiciones del wait

class LoginPage:

    #url de la pagina a probar
    URL = "https://www.saucedemo.com/"

    #locators es la forma de identificar a los elementos en la pagina web
    #para nosotros despues interactuar con ellos a traves de selenium y poder utilizarlos
    #si los atributos cambian aca es donde hay que venir a cambiar los

    _USER_INPUT = (By.ID,"user-name")
    _PASS_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")

    #defino una funcion _init_ y paso por parametro self y driver, 
    #self dentro de una clase nos referimos a nosotros mismos
    #es como si estuviesemos ejecutando alguna funcion dentro de esta clase
    #dentro del al estructura de una clase cuando hago una funcion primero me llamo a mi mismo y despues al driver

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    #hago una funcion solo para abrir el navegador uso self para luego utilizar la url
    def abrir_pagina(self):
        self.driver.get(self.URL)# de esta forma estaria inicializando la pagina
        return self
    
    #funcion para completar los datos del usuario para el login
    def completar_user(self,usuario):
        input = self.wait.until(EC.visibility_of_element_located(self._USER_INPUT))
        input.clear()
        input.send_keys(usuario)
        return self
    
    def completar_pass(self,password):
        input = self.driver.find_element(*self._PASS_INPUT)#el asterisco delante de una variable es que va a desempaquetar, find_element necesita dos valores By.ID,"user-name", ID y user-name por eso necesita desempaquetar a la variable que contiene esos dos elementos en este caso seria _PASS_INPUT
        input.send_keys(password)
        input.clear()                                      
        return self
    
    def hacer_click_button(self):
        self.driver.find_element(*self._LOGIN_BUTTON).click()

    def login_completo(self,usuario,password):
        self.completar_user(usuario)
        self.completar_pass(password)
        self.hacer_click_button()
        return self