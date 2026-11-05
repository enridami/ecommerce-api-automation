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


def test_get_product_by_id(api_client):
    """Valida la obtencion de un producto especifico mediante su ID."""
    product_id = 1

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
    
    payload = {
        "title": "New QA Automation T-Shirt",
        "price": 25,
        "description": "Una remera genial para ingenieros de QA.",
        "categoryId": 1,
        "images": ["https://placeimg.com/640/480/any"]
    }

    response = api_client.post(url, json=payload)

    # La API de Platzi responde con 201 Created al crear un recurso
    assert response.status_code == 201
    data = response.json()

    assert data["title"] == payload["title"]
    assert data["price"] == payload["price"]
    assert "id" in data

    print(f"\n[POST] Producto creado con ID: {data['id']}")


def test_update_product(api_client):
    """Valida la actualización parcial o total de un producto existente (PUT)."""
    product_id = 1  # Usamos un ID existente para la prueba de actualización
    url = f"{BASE_URL}/api/v1/products/{product_id}"
    
    payload = {
        "title": "Updated Majestic Mountain T-Shirt"
    }
    
    response = api_client.put(url, json=payload)
    
    assert response.status_code == 200
    data = response.json()
    
    assert data["title"] == payload["title"]
    print(f"\n[PUT] Producto {product_id} actualizado a: {data['title']}")


def test_delete_product(api_client):
    """Valida la eliminación de un producto (DELETE)."""
    product_id = 1
    url = f"{BASE_URL}/api/v1/products/{product_id}"
    
    response = api_client.delete(url)
    
    # La API de Platzi responde con 200 y un booleano (true) al eliminar exitosamente
    assert response.status_code == 200
    data = response.json()
    
    assert data is True or data == {"status": True}
    print(f"\n[DELETE] Producto con ID {product_id} eliminado correctamente.")