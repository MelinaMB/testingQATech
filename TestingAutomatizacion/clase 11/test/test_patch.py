import requests
import pytest

@pytest.mark.api
def test_patch_users(url_base,header_request):
    #vamos a utilizar la api reqres.in
    url = f'{url_base}/2'

    payload = {"name":"Jose"}
    response = requests.patch(url,headers=header_request,json=payload)


    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")

    #validacion status code
    assert response.status_code == 200

    #validacion de datos
    body = response.json()
    assert body["name"] == payload["name"]