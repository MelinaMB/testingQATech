#
from selenium.webdriver.common.by import By #By te permite localizar elementos usando diferentes estrategias(ID, CSS, XPath, etc)
from selenium.webdriver.support.ui import WebDriverWait #importa la espera 
from selenium.webdriver.support import expected_conditions as EC #importa las condiciones que puedes esperar (elemento visible, clickable, etc.)
import time

class LoginPage:

    #url de la pagina a probar la defino como una constante
    URL = "https://www.saucedemo.com/"

    #Locators
    #locators es la forma de identificar a los elementos en la pagina web
    #para nosotros despues interactuar con ellos a traves de selenium y poder utilizarlos
    #si los atributos cambian aca es donde hay que venir a cambiar los
    #los locators se definen como tuplas(estrategia, valor)
    #las variables que empiezan con _(guion bajo) son "privadas" por convención

    _USER_INPUT = (By.ID,"user-name")
    _PASS_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")

    #defino una funcion _init_ y paso por parametro self y driver, 
    #self dentro de una clase nos referimos a nosotros mismos
    #es como si estuviesemos ejecutando alguna funcion dentro de esta clase
    #dentro del al estructura de una clase cuando hago una funcion primero me llamo a mi mismo y despues al driver
    #este es el constructor ambos guion bajo van dobles, se va a ejecutar automaticamente cuando creo una instancia
    def __init__(self, driver):
        self.driver = driver #guardo el driver como atributo de la instancia. Aca self.driver se convierte en un atributo del objeto
        self.wait = WebDriverWait(driver, 10) #creo un WebDriverWait con timeout de 10 segundos. Otro atributo

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
        time.sleep(3)
        self.hacer_click_button()
        return self
    
    #aca debe estar la funcion de capturar el mensaje de error
    def obtener_error(self):
        div_error = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".error-message-container h3")))
        return div_error.text