import requests
from config.config import BASE_URL

def test_get_all_products(api_client):
    """Valida que se puede obtener la lista de productos correctamente."""
    response = api_client.get(f"{BASE_URL}/api/v1/products")

    # Validar código de estado 200 OK
    assert response.status_code == 200

    data = response.json()

    # Validar que la respuesta sea una lista y contenga elementos
    assert isinstance(data, list)
    assert len(data) > 0

    # Validar la estructura del primer producto
    assert "id" in data[0]
    assert "title" in data[0]
    assert "price" in data[0]

    print(f"\nTotal de productos obtenidos: {len(data)}")
    print(f"Primer producto: {data[0]['title']}")

