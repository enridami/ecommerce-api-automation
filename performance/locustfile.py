from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    # Tiempo de espera simulado en segundos
    wait_time = between(1, 3)

    @task(3)
    def get_all_products(self):
        """Simula a un usuario consultando el catalogo de productos (Petición GET)"""
        self.client.get("/api/v1/products")

    @task(1)
    def get_single_product(self):
        """Simula a un usuario buscando un producto específico por ID."""
        product_id = 1
        self.client.get(f"/api/v1/products/{product_id}")