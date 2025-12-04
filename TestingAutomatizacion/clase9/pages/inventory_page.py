from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait #importa la espera
from selenium.webdriver.support import expected_conditions as EC #importa las condiciones del wait
import time

class InventoryPage:

    #Selectores

    _INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    _ADD_TO_CART_BOTTON = (By.CLASS_NAME, "btn_inventory")
    _CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    _CART_COUNT = (By.CLASS_NAME, "shopping_cart_badge")
    _INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

#voy a capturar todos los productos del inventario 
    def obtener_todos_los_productos(self):
        self.wait.until(EC.visibility_of_all_elements_located(self._INVENTORY_ITEMS))#aca hago la espera me aseguro que los elementos aparezcan
        productos = self.driver.find_elements(*self._INVENTORY_ITEMS)#traigo todos los elementos
        return productos

    def obtener_nombres_productos(self):
        productos = self.driver.find_elements(*self._ITEM_NAME)#aca obtengo todos los elementos en forma de lista, necesito recorrerlos uno por uno para poder utilizarlos
        return [producto_nombre.text for producto_nombre in productos]

    def agregar_primer_producto(self):
        productos = self.wait.until(EC.visibility_of_all_elements_located(self._INVENTORY_ITEMS))#obtengo los elementos

        primer_boton_producto = productos[0].find_element(*self._ADD_TO_CART_BOTTON)#busco el elemento boton
        primer_boton_producto.click()#hago click en el boton
        return self

    def agrgar_producto_por_nombre(self,nombre_producto):
        self.wait.until(EC.visibility_of_all_elements_located(self._INVENTORY_ITEMS))
        productos = self.driver.find_elements(*self._INVENTORY_ITEMS)

        for producto in productos:
            nombre = producto.find_element(*self._INVENTORY_ITEM_NAME).text

            if nombre.strip().lower() == nombre_producto.strip().lower(): #estoy validando lo que yo tengo en mi pagino con lo que yo le estoy pasando
                boton = producto.find_element(*self._ADD_TO_CART_BOTTON)
                boton.click()
                return self
            
        raise Exception(f"No se encontro el producto{nombre_producto}")
        
    def abrir_carrito(self):
        self.wait.until(EC.element_to_be_clickable(self._CART_BUTTON)).click()
        return self

    def obtener_conteo_carrito(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self._CART_COUNT))
            contador_carrito = self.driver.find_element(*self._CART_COUNT)
            return int(contador_carrito.text)
        except:
            return 0