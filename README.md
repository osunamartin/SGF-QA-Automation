🎯 Objetivo

Este repositorio contiene pruebas automatizadas para el sistema Gestión Farmacias, incluyendo:

✅ UI Testing (Playwright)

✅ API Testing (requests)

✅ DB Testing (MySQL)

✅ E2E Tests (DB → UI)

El objetivo es validar el funcionamiento del sistema de forma reproducible y escalable.

🧰 Tecnologías

Python 3.11+

Pytest

Playwright (Python)

python-dotenv

mysql-connector-python

(Opcional) requests para API testing

⚙️ Requisitos previos

Tener levantado el sistema Gestión Farmacias:

Frontend: http://localhost:3000

Backend/API: http://localhost:3001 (si aplica)

Base de datos MySQL funcionando

🐍 Setup del entorno (Windows)
1) Crear y activar el venv
python -m venv venv
.\venv\Scripts\activate

2) Instalar dependencias
pip install -r requirements.txt

3) Instalar navegadores de Playwright
python -m playwright install

🔐 Configuración .env

Crear un archivo .env en la raíz del proyecto:

BASE_URL=http://localhost:3000

DB_HOST=127.0.0.1
DB_USER=root
DB_PASS=TU_PASSWORD
DB_NAME=farmacia_db
DB_PORT=3306

▶️ Ejecutar tests
Correr todo:
pytest -v

Correr solo UI:
pytest -v tests/ui

Correr solo DB:
pytest -v tests/db

Correr solo E2E:
pytest -v tests/e2e

🧪 Cómo funciona la estrategia de datos (DB Fixture)

El proyecto usa un fixture en conftest.py llamado test_product.

¿Qué hace?

Inserta un producto real en la tabla productos

Devuelve un diccionario con los datos creados

Al finalizar el test, borra ese producto

Esto permite:

✅ crear datos de prueba limpios
✅ evitar contaminación de base
✅ ejecutar tests repetibles

🧠 ¿Qué es conftest.py?

Archivo especial de pytest.

Sirve para definir:

fixtures globales

setup/teardown automático

configuraciones compartidas

🧩 Fixtures importantes
db_connection

Conecta una sola vez a la DB durante toda la sesión.

test_product

Crea 1 producto único por test y lo elimina al finalizar.

page

Crea una instancia de Playwright lista para usar.

🧼 Buenas prácticas usadas

Datos de prueba únicos (uuid)

Cleanup automático (yield)

Tests independientes

Separación por capas: UI / API / DB / E2E

🚧 Limitaciones actuales del sistema (del proyecto original)

No hay CRUD UI completo

No hay carga de CSV desde UI

No hay login

El sistema depende fuertemente de datos precargados

Por eso los tests E2E se apoyan en DB.

