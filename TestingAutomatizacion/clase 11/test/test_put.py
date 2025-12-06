import requests
import time
import pytest

@pytest.mark.api
#@pytest.mark.skip(reason="Desactivada porque sigue en desarollo") puedo saltear un test utilizando el marcador skip
def test_put_users():
    encabezado = {"x-api-key": "reqres_be64950124cf4da780382775b0a9adcb"}

#vamos a utilizar la api reqres.in
    url = 'https://reqres.in/api/users/2'

    payload = {"name":"Jose","Job":"Profesor"}

    #para usar el time tengo que definir cuando arranca esta funcion, tengo que definirla antes del put
    inicio = time.time()
    response = requests.put(url,headers=encabezado,json=payload)
    #defino para time despues del put la diferencia entre el tiempo en el momento contra la diferencia que tengo al inicio, en total me da lo que tarda el put
    tiempo_diff = time.time() - inicio
    

    assert response.status_code == 200

    #validacion de tiempo de respuesta
    assert tiempo_diff < 2, f"La api tardo demasiado {tiempo_diff}"#f es para formato string me permite concatenar string con otros datos

    #validacion de datos
    body = response.json()

    assert "updatedAt" in body
    #validacion de datos
    assert isinstance(body["name"],str) #funcion de pytest, valido que los datos sean string, desde el body le pido el dato name

    #podemos comparar un dato con el que me esta devolviendo el servidor
    assert body["name"] == payload["name"]