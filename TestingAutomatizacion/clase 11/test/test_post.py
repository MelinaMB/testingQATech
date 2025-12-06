import requests
import pytest

@pytest.mark.api
def test_post_users(url_base,header_request):
    #vamos a utilizar la api reqres.in
    url = f'{url_base}'


    

    payload = {"name":"Jose","job":"Profesor"}
    response = requests.post(url,headers=header_request,json=payload)

    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")

    #valido que el recurso se creo
    assert response.status_code == 201
    data = response.json()

    #verificar que el nombre de la respuesta sea el mismo que el enviado
    assert data["name"] == payload["name"]#payload es el cuerpo de la solicitud desde el cliente
                                        #y data["name"] es el nombre que viene del servidor

    #verificar que la respuesta tenga un id
    assert "id" in data

