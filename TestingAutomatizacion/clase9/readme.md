# Proyecto de Talento Tech
## Proposito del proyecto
Este proyecto tiene como objetivo automatizar pruebas de UI y de API para el sitio SauceDemo, aplicando practicas como Page Object Model, manejo de datos externos, generacion de reportes HTML, logging y captura automatica de pantalla.
## Tecnologias utilizadas
- Pythin 3.x
- Pytest
- Selenium WebDriver
- Logging
- Faker 
- CSV / JSON
- Resquest 

## Reportes y Logs
El proyecto genera tres tipos principales de resultados durante la ejecucion de las pruebas:
**reporte HTML**, **capturas de pantalla**, **archivo de log**

## Reporte HTML
Se genera un reporte HTML detallado con el nombre de ```reporte.html``` en la **carpeta raiz** del proyecto

## Logs de ejecucion
Se genera un log con informacion detallada de todas las pruebas en la siguiente ubucacion:
```logs/suite.log```

## Capturas de pantalla
se realizan capturas de pantalla por cada test que haya fallado, se encuentra en la siguiente ubicacion 
```reports/screens/```

## Ejecutar todas las pruebas
Para iniciar la ejecucion de las pruebas debes ejecutar la siguiente linea:
```bash
python -m run_test.py
```

## ¿Comó interpretar los reportes?
- Al ejecutar el ```run_test.py```, se genera un archivo html en la carpeta raiz.
- El reporte incluye:
    - Lista completa de test ejecutados 
    - El estado de cada prueba
    - La duracion de cada test
    - Las capturas de pantalla para pruebas fallidas

## Pruebas incluidas
- Login exitoso y fallido
- Login exitoso y fallido usando faker
- comportamiento de la pagina de inventario
- Comportamiento de la pagian del carrito
- API (Reqres): GET users, POST create user, DELETE user, validaciones de codigos HTTP, validaciones de estructura JSON

## Manejo de datos de prueba
- En la carpeta ```datos``` se incluyen archivos como:
    -`data_login.csv` -> datos de usuario validos o invalidos
    -`productos.json`-> datos de productos para validacion
### Conclusion
Este proyecto ofrece una estructura organizada y escalable para automatizar purebas de API utilizando Python, Pytest y Selenium.
Posee un flujo continuo de pruebas mediante el archivo `run_test.py`, con una generacion automatica de reporte HTML facilitando el analisis de las pruebas.
La arquitectura del proyecto esta pensada para generar nuevos casos de prueba y configuraciones sin modificar el nucleo del proyecto. De esta manera se mantienen buenas practicas y permite la escalabilidad en el tiempo. 