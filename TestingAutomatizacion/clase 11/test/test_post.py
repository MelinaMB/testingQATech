import requests

def test_post_users():
    #vamos a utilizar la api reqres.in
    url = 'https://reqres.in/api/users'


    encabezado = {"x-api-key": "reqres_be64950124cf4da780382775b0a9adcb"}#autorizacion para pode uzar la api https://reqres.in/signup

    payload = {"name":"Jose","job":"Profesor"}
    response = requests.post(url,headers=encabezado,json=payload)

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

