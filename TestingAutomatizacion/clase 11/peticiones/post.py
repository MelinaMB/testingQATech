import requests

encabezado = {"x-api-key": "reqres_be64950124cf4da780382775b0a9adcb"}#autorizacion para pode uzar la api https://reqres.in/signup

#vamos a utilizar la api reqres.in
url = 'https://reqres.in/api/users'

data = {"name":"Jose","Job":"Profesor"}
response = requests.post(url,headers=encabezado,json=data)

print(response.status_code)
print(response.json())