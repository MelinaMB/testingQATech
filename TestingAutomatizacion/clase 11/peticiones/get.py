#vamos a trbajar con una libreria que nos prmite interactur con apis http
import requests

encabezado = {"x-api-key": "YOUR_API_KEY"}#autorizacion para pode uzar la api https://reqres.in/signup

#vamos a utilizar la api reqres.in
url = 'https://reqres.in/api/users?page=2'

response = requests.get(url,headers=encabezado,verify=False)#ver para que es verify=False

print(response.status_code)#veo la respuesta


data = response.json()#el cuerpo de la en formato json
print(data)

