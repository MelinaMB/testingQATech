import requests

encabezado = {"x-api-key": "reqres_be64950124cf4da780382775b0a9adcb"}

#vamos a utilizar la api reqres.in
url = 'https://reqres.in/api/users/2'

payload = {"name":"Jose","Job":"Profesor"}

response = requests.put(url,headers=encabezado,json=payload)

print(response.status_code)
print(response.json())