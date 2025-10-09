import pytest 
#import main #el archivo que quiero hacer el test
from calculadora import suma, resta, division, multiplicacion # importo las funciones que quiero probar

# de esta forma se hace uno por uno las pruebas casda assert es una prueba 
# y cada assert lleva sus parametros
#def test_suma():
#    assert  suma(2, 3) == 5 #nos va a permitir validar la prueba con datos de entrada y datos de salida
#    assert suma(5, 3) == 40
#-----------------------------------------------------------------
#parametrizacion tambien es una etiqueta

@pytest.mark.criticos
@pytest.mark.parametrize("a,b,resultado", [
    (10,5,15),
    (-6,3,-3),
    (2,4,6),
    (4,5,9)
])
def test_suma(a,b,resultado):
    assert suma(a,b) == resultado

def test_division_decimal():
    assert division(10,3) == pytest.approx(3.3333, rel=1e-3)

#manejador de errores 
#en este caso no se puede dividir por cero
@pytest.mark.manejoError
def test_division_cero():
    with pytest.raises(ZeroDivisionError):
        division(10,0)

@pytest.mark.skip(reason="funcionalidad aun no implementada")
def test_resta():
    assert resta(2,3) == 5