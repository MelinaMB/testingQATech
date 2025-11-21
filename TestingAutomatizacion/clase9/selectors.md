| Elemento                       | id/name/class                  | Selector css
------------                     |-----------                     |---------------
input usuario                    | user-name                      | #user-name
input password                   | password                       | #password
boton login                      | submit                         | input[type='submit']

titulo                           | title                          | title
primer producto                  | inventory_item                 | .inventory_item
menu hamburguesa                 | react-burger-menu-btn          | #react-burger-menu-btn
filtro                           | product_sort_container         | .product_sort_container
opcion de filtro A to Z          | az                             | select_by_value("az")
opcion de filtro low to high     | lohi                           | select_by_value("lohi")

cantidad de elemento del carrito | shoping_cart_badge             | .shopping_cart_badge
boton de add to cart             | add-to-cart-sauce-labs-backpack|#add-to-cart-sauce-labs-backpack
boton de carrito                 | shopping_cart_link             | .shpping_cart_link
cart item                        | cart_item                      | .cart_item
nombre del item                  | inventory_item_name            | .inventory_item_name


El proposito del proyecto es evaluar un pagina web https://www.saucedemo.com/ realizar test para login,la navegacion y el carrito.
Se van a utilizar tegnologias como: python, pytest, selenium, webdriver, pytest html

Para la instalacion de las dependencias:
pytest: pip install pytest
Selenium: pip install selenium
Webdriver: pip install webdriver-manager
pytest html: pip install pytest -html

Para ejecutar la purebas:
pytest test_nombre_del_Archivo.py

Para ejecutar el run_test.py con el report
pytest --html=report.html --self-contained-html
