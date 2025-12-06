#herramienta que nos permite registrar la informacion durante una ejecucion de cualquier test

import logging
import pathlib

audir_dir = pathlib.Path('logs')
#evaluo si la carpeta de logs existe o creo una
audir_dir.mkdir(exist_ok=True)

#creo el archivo log
log_file = audir_dir/ 'suite.log'

logger = logging.getLogger("Talento tech")#estamos evaluando si existe el logger
#establezco que tipo de mensaje va a manejar este logger
logger.setLevel(logging.INFO)

if not logger.handlers: 
    file_handler = logging.FileHandler(log_file, mode = "a", encoding="utf-8")# lo que hace el modo a(append) es abrir el archivo y a medida que se van ejecutando los test se va escribiendo uno arriba del otro

    #defino el formato que se va a escribir linea a linea
    formatter = logging.Formatter(

        "%(asctime)s %(levelname)s %(name)s %(message)s",#la s es como el especificador del formato
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
