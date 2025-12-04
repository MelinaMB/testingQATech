import requests

def test_get_users():
    encabezado = {"x-api-key": "YOUR_API_KEY"}#autorizacion para pode uzar la api https://reqres.in/signup

#vamos a utilizar la api reqres.in
    url = 'https://reqres.in/api/users?page=2'

    response = requests.get(url,headers=encabezado)

    #valido que la respuesta sea existosa
    assert response.status_code == 200

    data = response.json()

    #verificar que la clave data esta presente
    assert "data" in data #va a buscar la clave "data" en el json que se encuentra en la variable data

    #verificar que haya al menos un usuario en la lista
    assert len(data["data"]) > 0 #pido que me muestre lo que hay en la clave data
    
    #verificar que data es una lista
    assert isinstance(data["data"],list)
    