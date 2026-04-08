ENG

🎯 Objective

This repository contains automated tests for the Pharmacy Management System
, including:

✅ UI Testing (Playwright)

✅ API Testing (requests)

✅ DB Testing (MySQL)

✅ E2E Tests (DB → UI)

The goal is to validate the system’s behavior in a reproducible and scalable way.

📝 Manual Testing Documentation

Pharmacy Management System - Manual Testing

🧰 Technologies

Python 3.11+

Pytest

Playwright (Python)

python-dotenv

mysql-connector-python

Requests for API testing

⚙️ Prerequisites

Have the Pharmacy Management System
 up and running:

Frontend: http://localhost:3000

Backend/API: http://localhost:3001
 (if applicable)

MySQL database running

🐍 Environment setup (Windows)
Create and activate the venv
python -m venv venv
.\venv\Scripts\activate
Install dependencies
pip install -r requirements.txt
Install Playwright browsers
python -m playwright install
🔐 .env Configuration

Create a .env file in the project root:

BASE_URL=http://localhost:3000

DB_HOST=127.0.0.1
DB_USER=root
DB_PASS=YOUR_PASSWORD
DB_NAME=farmacia_db
DB_PORT=3306

▶️ Run tests

Run all:
pytest -v

Run only UI:
pytest -v tests/ui

Run only DB:
pytest -v tests/db

Run only E2E:
pytest -v tests/e2e

🧪 How the data strategy works (DB Fixture)

The project uses a fixture in conftest.py called test_product, which inserts a real product into the productos table and returns a dictionary with the created data.

At the end of the test, it deletes that product.

This allows:

✅ Creating clean test data
✅ Avoiding database contamination
✅ Running repeatable tests even when the database has no products

🧩 Important fixtures
db_connection:

Connects to the DB once per session.

test_product

Creates 1 unique product per test and deletes it at the end.

page

Creates a ready-to-use Playwright instance.

🧼 Best practices used

Unique test data (uuid)

Automatic cleanup (yield)

Independent tests

Layer separation: UI / API / DB / E2E

🚧 Current system limitations (from the original project)

No complete UI CRUD

No CSV upload from UI

No login

The system heavily depends on preloaded data

E2E tests rely on the database because of this

----

ESP

## 🎯 Objetivo

Este repositorio contiene pruebas automatizadas para el [Sistema Gestión Farmacias](https://github.com/nnvelez95/Gestion-Farmacias), incluyendo:

✅ UI Testing (Playwright)

✅ API Testing (requests)

✅ DB Testing (MySQL)

✅ E2E Tests (DB → UI)

El objetivo es validar el funcionamiento del sistema de forma reproducible y escalable.

## 📝 Documentación de Pruebas Manuales

[Sistema Gestión Farmacias - Testing Manual](https://docs.google.com/spreadsheets/d/1gVgSQkQUnCyBSVGTIMV64B14QOo20DI5atE8N8INsO8/edit?gid=359185771#gid=359185771)

## 🧰 Tecnologías

Python 3.11+

Pytest

Playwright (Python)

python-dotenv

mysql-connector-python

Requests para API testing 

## ⚙️ Requisitos previos

Tener levantado el [Sistema Gestión Farmacias](https://github.com/nnvelez95/Gestion-Farmacias):

Frontend: http://localhost:3000

Backend/API: http://localhost:3001 (si aplica)

Base de datos MySQL funcionando

## 🐍 Setup del entorno (Windows)
1) Crear y activar el venv
python -m venv venv
.\venv\Scripts\activate

2) Instalar dependencias
pip install -r requirements.txt

3) Instalar navegadores de Playwright 
python -m playwright install

## 🔐 Configuración .env

Crear un archivo .env en la raíz del proyecto:

BASE_URL=http://localhost:3000

DB_HOST=127.0.0.1
DB_USER=root
DB_PASS=TU_PASSWORD
DB_NAME=farmacia_db
DB_PORT=3306

## ▶️ Ejecutar tests
Correr todo:
pytest -v

Correr solo UI:
pytest -v tests/ui

Correr solo DB:
pytest -v tests/db

Correr solo E2E:
pytest -v tests/e2e

## 🧪 Cómo funciona la estrategia de datos (DB Fixture)

El proyecto usa un fixture en conftest.py llamado test_product, el cual inserta un producto real en la tabla productos y devuelve un diccionario con los datos creados.

Al finalizar el test, borra ese producto

Esto permite:

✅ Crear datos de prueba limpios
✅ Evitar contaminación de base
✅ Ejecutar tests repetibles aún cuando la base de datos no contenga productos

## 🧩 Fixtures importantes

### db_connection:

Conecta una sola vez a la DB durante toda la sesión.

### test_product

Crea 1 producto único por test y lo elimina al finalizar.

### page

Crea una instancia de Playwright lista para usar.

## 🧼 Buenas prácticas usadas

Datos de prueba únicos (uuid)

Cleanup automático (yield)

Tests independientes

Separación por capas: UI / API / DB / E2E

## 🚧 Limitaciones actuales del sistema (del proyecto original)

No hay CRUD UI completo

No hay carga de CSV desde UI

No hay login

El sistema depende fuertemente de datos precargados

Los tests E2E se apoyan en base de datos debido a esto.





