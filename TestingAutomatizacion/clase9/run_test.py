import pytest
#va a tener los archivos de las pruebas a ejecutar
test_files = [
    "tests/test_login.py",
    "tests/test_navegacion.py",
    "tests/test_carrito"
]

pytest_args = test_files + ["--html=report.html","--self-contained-html","-v"]

#"--self-contained-html"se utiliza para olvidarnos del css o el javascript que va a tener el reporte
#-v es para obtener el detalle de la informacion de los test
#todo esto se guarda en una variable en este caso pytest_args y se manda a pytest.main para que corra todos los test 
pytest.main(pytest_args)