# API QA Automation Framework (Platzi Fake Store)

![API QA Automation CI](https://github.com/enridami/ecommerce-api-automation/actions/workflows/ci.yml/badge.svg)
[![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/testing-pytest-orange.svg)](https://docs.pytest.org/)
[![Locust](https://img.shields.io/badge/performance-locust-green.svg)](https://locust.io/)

Este proyecto consiste en el diseño, desarrollo e implementación de un **Framework de Pruebas Automatizadas de Extremo a Extremo (E2E)** para evaluar la API REST pública de *Platzi Fake Store*. 

El objetivo principal fue construir un ecosistema de calidad robusto, modular y mantenible bajo estándares de ingeniería de software, cubriendo desde la validación de endpoints funcionales hasta la simulación de carga masiva y la integración en flujos de trabajo en la nube (CI/CD).


## Trabajo Realizado (Alcance Técnico)

Para llevar este proyecto a un estándar profesional de automatización, se ejecutaron las siguientes fases de desarrollo:

* **Pruebas Funcionales y Ciclo de Vida CRUD:** Automatización de flujos completos de creación, lectura, actualización y eliminación de productos (POST, GET, PUT, DELETE) utilizando `Requests` y `Pytest`.
* **Aislamiento Dinámico de Datos:** Implementación de datos de prueba únicos (mediante UUIDs) para asegurar que cada ejecución sea independiente, idempotente y no dependa de estados compartidos en la base de datos de la API.
* **Validación de Contratos (Contract Testing):** Integración de `JSON Schema` para auditar que la estructura, tipos de datos y propiedades de las respuestas JSON del backend cumplan de forma estricta con las especificaciones esperadas.
* **Pruebas Negativas y Manejo de Errores Parametrizados:** Diseño de matrices de prueba para evaluar la resiliencia de la API ante payloads malformados, datos inválidos y límites de entrada, validando códigos de respuesta HTTP adecuados (400, 404, 422).
* **Evaluación de Rendimiento y Carga:** Simulación de concurrencia de usuarios mediante `Locust` para medir métricas clave de comportamiento del sistema como solicitudes por segundo (RPS), latencias y percentil 95 (P95).
* **Orquestación de CI/CD (Integración Continua):** Configuración desatendida mediante **GitHub Actions** para ejecutar automáticamente toda la suite de pruebas en un entorno virtual limpio de Linux (Ubuntu) tras cada commit o Pull Request.

## Arquitectura del Proyecto


```text
ecommerce-api-automation/
│
├── .github/
│   └── workflows/
│       └── ci.yml          # Pipeline de Integración Continua (GitHub Actions)
├── performance/
│   └── locustfile.py       # Simulación de carga y usuarios concurrentes
├── schemas/
│   └── product_schema.py   # Definición de contratos JSON Schema
├── tests/
│   ├── test_crud.py        # Pruebas funcionales de operaciones CRUD (Aislamiento de datos)
│   └── test_errors.py      # Pruebas negativas y parametrizadas (Manejo de códigos de error)
├── requirements.txt        # Dependencias limpias y multiplataforma del proyecto
└── pytest.ini              # Configuración global del motor de pruebas
```
---
## Tecnologías y Herramientas Utilizadas

- Python

- Pytest

- Requests

- JSON Schema

- Locust

- GitHub Actions



## Guía de Instalación y Configuración Local
### 1. Clonar el repositorio
```
git clone [https://github.com/tu-usuario/ecommerce-api-automation.git](https://github.com/enridami/ecommerce-api-automation.git)
cd ecommerce-api-automation
```

### 2. Crear y activar un entorno virtual
En Windows: 
```
python -m venv venv
venv\Scripts\activate
```

En macOS / Linux: 
```
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias
```
pip install --upgrade pip
pip install -r requirements.txt
```


## Ejecución de Pruebas
### 1. Ejecutar la suite de pruebas funcionales y de contratos
Para correr todas las pruebas con salida detallada (-v):
```
pytest -v -s
```

### 2. Ejecutar las pruebas de rendimiento y carga con Locust
Para levantar la interfaz gráfica y simular usuarios concurrentes:
```
locust -f performance/locustfile.py --host=[https://api.escuelajs.co](https://api.escuelajs.co)
```



## Integración Continua (CI/CD)
El proyecto cuenta con un pipeline automatizado en GitHub Actions (.github/workflows/ci.yml) que se ejecuta en cada push o Pull Request sobre la rama principal, garantizando que el entorno de Linux verifique la integridad de las pruebas de forma desatendida.

![API QA Automation CI](https://github.com/enridami/ecommerce-api-automation/actions/workflows/ci.yml/badge.svg)