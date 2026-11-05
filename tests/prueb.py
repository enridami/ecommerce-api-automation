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