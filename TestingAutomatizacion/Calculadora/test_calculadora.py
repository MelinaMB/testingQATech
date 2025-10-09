import pytest 
#import main #el archivo que quiero hacer el test
from calculadora import suma, resta, division, multiplicacion # importo las funciones que quiero probar


def test_suma():
    assert  suma(2, 3) == 5 #nos va a permitir validar la prueba con datos de entrada y datos de salida
    assert suma(5, 3) == 40