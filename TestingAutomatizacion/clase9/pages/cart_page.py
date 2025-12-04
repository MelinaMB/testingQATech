from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait #importa la espera
from selenium.webdriver.support import expected_conditions as EC #importa las condiciones del wait
import time

class CartPage:

    _CART_ITEMS = (By.CLASS_NAME, "cart_item")
    _CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")


    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def obtener_productos_carrito(self):
        productos = self.wait.until(EC.visibility_of_all_elements_located(self._CART_ITEMS))
        return productos
    
    def obtener_nombre_producto_carrito(self):
        
        try:
        # Primero verificar si hay elementos del carrito
            productos = self.driver.find_elements(*self._CART_ITEMS)
        
            if not productos:  # Si no hay productos
                return []  # Devolver lista vacía
        
        # Si hay productos, extraer sus nombres
            nombres_productos = []
            for producto in productos:
                try:
                    nombre = producto.find_element(*self._CART_ITEM_NAME).text
                    nombres_productos.append(nombre)
                except:
                # Si no puede encontrar el nombre en este producto, continuar
                    continue
        
            return nombres_productos
    
        except Exception as e:
            print(f"Error obteniendo productos del carrito: {e}")
            return []  # Devolver lista vacía en caso de error
    
