import pytest
import requests
from lambda_forge.constants import BASE_URL


@pytest.mark.integration(method="GET", endpoint="/hello_jhony")
def test_hello_jhony_status_code_is_200():

    response = requests.get(url=f"{BASE_URL}/hello_jhony")

    assert response.status_code == 200
