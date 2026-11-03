import pytest
import requests
from config.config import BASE_URL

@pytest.fixture(scope="session")
def api_client():
    """Fixture que crea una sesión HTTP reutilizable para todas las pruebas."""
    session = requests.Session()
    # Configuración de headers globales que usarán todas las peticiones
    session.headers.update({"Content-type": "application/json"})

    session.base_url = BASE_URL

    yield session  # Se entrega el cliente a la prueba
    session.close() # Se cierra la sesión al terminar todas las pruebas