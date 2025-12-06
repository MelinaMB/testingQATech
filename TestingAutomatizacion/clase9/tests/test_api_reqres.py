import requests
import pytest
from utils.logger import logger
#Obtener usuario
def test_get_user(url_base,header_request):#el url_base me lleva a una lista de usuarios
    logger.info("Realizando la solicitus GET a {url_base}")
    response = requests.get(f"{url_base}/2",headers=header_request)#estoy trayendo un usuario el 2

    assert response.status_code == 200

    data = response.json()

    assert data["data"]["id"] == 2 

def test_create_user(url_base,header_request):
    payload={
        "name": "Pepe",
        "Job": "Profesor"
    }
    response = requests.post(url_base,headers=header_request,json=payload)

    assert response.status_code == 201
    data = response.json()

    assert data["name"] == payload["name"]

def test_delete_user(url_base,header_request):
    response = requests.delete(f"{url_base}/2",headers=header_request)

    assert response.status_code == 204