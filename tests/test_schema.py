import pytest
from jsonschema import validate
from config.config import BASE_URL
from schemas.product_schema import PRODUCT_SCHEMA

def test_get_product_schema(api_client):
    """Valida que la estructura del producto cumpla con el esquema JSON definido."""
    product_id = 4
    url = f"{BASE_URL}/api/v1/products/{product_id}"
    
    response = api_client.get(url)
    assert response.status_code == 200
    
    product_data = response.json()
    
    # Cmparamos el JSON real contra el de product_data
    validate(instance=product_data, schema=PRODUCT_SCHEMA)
    
    print(f"\n[SCHEMA] El esquema del producto ID {product_id} es válido y cumple con el contrato.")