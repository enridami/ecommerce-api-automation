import pytest
from config.config import BASE_URL

INVALID_IDS = [
    ("abc", 400),      # ID de tipo texto (la API espera un número)
    (-1, 400),         # ID negativo
    (999999, 400)      # ID numérico inexistente en la base de datos
]

@pytest.mark.parametrize("invalid_id, expected_status", INVALID_IDS)
def test_get_product_invalid_ids(api_client, invalid_id, expected_status):
    """
    Prueba parametrizada negativa: Valida que la API responda con el 
    código de error correcto al intentar buscar productos con IDs inválidos.
    """
    url = f"{BASE_URL}/api/v1/products/{invalid_id}"
    
    response = api_client.get(url)
    
    assert response.status_code == expected_status

    print(f"\n[NEGATIVO] ID provocado: {invalid_id} -> Código obtenido correctamente: {response.status_code}")