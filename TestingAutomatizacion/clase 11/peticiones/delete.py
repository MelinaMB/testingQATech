import requests

encabezado = {"x-api-key": "reqres_be64950124cf4da780382775b0a9adcb"}

#vamos a utilizar la api reqres.in
url = 'https://reqres.in/api/users/2'

response = requests.delete(url,headers=encabezado)

print(response.status_code)#respuesta 204 en no content 
#print(response.json())#no uso esta porque estoy borrando un recurso no resibo ningundato de la respuesta
print(response.text)
