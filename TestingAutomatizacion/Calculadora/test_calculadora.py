import pytest 
#import main #el archivo que quiero hacer el test
from calculadora import suma, resta, division, multiplicacion # importo las funciones que quiero probar

# de esta forma se hace uno por uno las pruebas casda assert es una prueba 
# y cada assert lleva sus parametros
#def test_suma():
#    assert  suma(2, 3) == 5 #nos va a permitir validar la prueba con datos de entrada y datos de salida
#    assert suma(5, 3) == 40
#-----------------------------------------------------------------
#fixture se preparan datos que luego voy a reutilizar
#los fixtures se van a declarar antes que las funciones a testear
@pytest.fixture
def numero ():
    return [1,2,3]

#se pueden desempaquetar los datos que puse en la funcion numero
def test_suma1(numero):
    a,b, c = numero
    assert a + b + c  == 6

#ver porque da error
#def test_suma2(numero):
 #   assert suma(numero) == 6

# el fixture tambien se puede aplicar a un ciclo
@pytest.fixture
def numeros():
    return [(1,2), (2,3), (5,2)]

def test_suma3(numeros):
    for a,b in numeros:
        resultado = a + b
        assert resultado == a + b

#otra forma de arreglo de datos
@pytest.fixture
def datos_entrada():
    return {
        "caso_positivo": (2,3),
        "caso_cero": (0,5),
        "caso_negativo": (-1,7)
    }
@pytest.mark.parametrize("clave, resultado_esperado", [
    ("caso_positivo",5),
    ("caso_cero", 5),
    ("caso_negativo", 6)
])
def test_suma4(datos_entrada, clave, resultado_esperado):
    a,b = datos_entrada[clave]
    assert suma(a, b) == resultado_esperado

@pytest.mark.parametrize("clave, resultado_esperado", [
    ("caso_positivo",-1),
    ("caso_cero", -5),
    ("caso_negativo", -8)
])
def test_resta2(datos_entrada, clave, resultado_esperado):
    a,b = datos_entrada[clave]
    assert resta(a, b) == resultado_esperado

#--------------------------------------------------------------------
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