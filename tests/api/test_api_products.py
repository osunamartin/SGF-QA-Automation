import os
import requests
from dotenv import load_dotenv

load_dotenv()


def test_api_products_returns_200():
    base_url = os.getenv("API_URL", "http://localhost:3000")

    r = requests.get(f"{base_url}/productos")

    assert r.status_code == 200
