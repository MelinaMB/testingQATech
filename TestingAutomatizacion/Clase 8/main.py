from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

#prueba de login con multiples usuarios
@pytest.mark.parametrize("username","password",[
    ("standard", "secret"),
    ("admin", "1234"),
    ("mod", "123")
])
def test_login(username,password):
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    #Localizacion e interaccion de elementos
    usuario = driver.find_element(By.ID, "user-name")
    usuario.send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()    

    driver.quit()