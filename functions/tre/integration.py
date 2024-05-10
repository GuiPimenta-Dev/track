import pytest
import requests
from lambda_forge.constants import BASE_URL


@pytest.mark.integration(method="GET", endpoint="/tre")
def test_tre_status_code_is_200():

    response = requests.get(url=f"{BASE_URL}/tre")

    assert response.status_code == 200
