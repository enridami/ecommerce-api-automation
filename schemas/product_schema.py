
PRODUCT_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "price": {"type": "number"},  # Permite int o float
        "description": {"type": "string"},
        "category": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "image": {"type": "string"},
                "creationAt": {"type": "string"},
                "updatedAt": {"type": "string"}
            },
            "required": ["id", "name"]
        },
        "images": {
            "type": "array",
            "items": {"type": "string"}
        },
        "creationAt": {"type": "string"},
        "updatedAt": {"type": "string"}
    },
    "required": ["id", "title", "price", "description", "category", "images"]
}