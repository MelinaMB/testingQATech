import csv
import os #es una libreria para leer el sistema, por ahora no la usamos
import pathlib

#vamos a recorrer a traves de un bucle linea por linea y guardar en una variable
#cada una de las cosas que nosotros fuimos capturando
def leer_csv_login(ruta_archivo):

    ruta = pathlib.Path(ruta_archivo)
    datos = []
    with open(ruta,newline='',encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            datos.append((fila["usuario"], fila["password"], fila["debe_funcionar"]))
    return datos

print(leer_csv_login("datos/data_login.csv"))