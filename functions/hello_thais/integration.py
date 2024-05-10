import pytest
import requests
from lambda_forge.constants import BASE_URL


@pytest.mark.integration(method="GET", endpoint="/hello_thais")
def test_hello_thais_status_code_is_200():

    response = requests.get(url=f"{BASE_URL}/hello_thais")

    assert response.status_code == 200
