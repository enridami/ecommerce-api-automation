import requests
import uuid
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


def test_get_product_by_id(api_client):
    """Valida la obtencion de un producto especifico mediante su ID."""
    product_id = 4

    response = api_client.get(f"{BASE_URL}/api/v1/products/{product_id}")

    assert response.status_code == 200
    data = response.json()

    assert data["id"] == product_id
    assert "title" in data
    assert "price" in data

    print(f"\n[GET ID] Producto obtenido exitosamente: {data['title']}")


def test_create_product(api_client):
    """Valida la creación de un nuevo producto (POST)"""
    url = f"{BASE_URL}/api/v1/products"

    # Identificador único corto para evitar colisiones de slug en la BD
    unique_suffix = uuid.uuid4().hex[:6]
    
    payload = {
        "title": f"New QA Automation T-Shirt {unique_suffix}",
        "price": 22,
        "description": "Una remera genial para ingenieros de QA.",
        "categoryId": 1,
        "images": [
            "https://i.imgur.com/ZANVnHE.jpeg"
        ]
    }


    response = api_client.post(url, json=payload)

    # Si la API rechaza la peticion, imprimimos el mensaje exacto del servidor
    if response.status_code != 201:
        print(f"\n[DEBUG] Respuesta del servidor: {response.text}")

    # La API de Platzi responde con 201 Created al crear un recurso
    assert response.status_code == 201
    data = response.json()

    assert data["title"] == payload["title"]
    assert data["price"] == payload["price"]
    assert "id" in data

    print(f"\n[POST] Producto creado con ID: {data['id']}")


def test_update_product(api_client):
    """Valida la actualización parcial o total de un producto existente (PUT)."""
    url = f"{BASE_URL}/api/v1/products"

    