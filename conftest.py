import sys
from pathlib import Path

import pytest
from utils.db import get_db_connection

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))


@pytest.fixture
def db_conn():
    conn = get_db_connection()
    yield conn
    conn.close()

import uuid
import pytest


import uuid
import pytest


@pytest.fixture
def test_product(db_conn):
    """
    Crea un producto único en la tabla productos.
    Devuelve un dict con los datos.
    Al finalizar el test, lo borra.
    """

    codigo = f"779{uuid.uuid4().hex[:10]}"   # algo tipo código de barras
    id_externo = f"QA-{uuid.uuid4().hex[:8]}"
    nombre = f"Producto QA {id_externo}"

    cur = db_conn.cursor()

    cur.execute(
        """
        INSERT INTO productos (
            id_externo,
            codigo_barras,
            troquel,
            nombre,
            droga,
            laboratorio,
            rubro,
            pvp,
            costo,
            margen,
            precio_pami,
            fecha_precio,
            stock_actual
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, CURDATE(), %s)
        """,
        (
            id_externo,
            codigo,
            "QA-TROQUEL",
            nombre,
            "Droga QA",
            "Lab QA",
            "Rubro QA",
            123.45,     # pvp
            80.00,      # costo
            35.00,      # margen
            0.00,       # precio_pami
            10          # stock_actual
        ),
    )

    db_conn.commit()
    cur.execute("SELECT id, codigo_barras, nombre FROM productos WHERE id_externo = %s", (id_externo,))
    row = cur.fetchone()
    print("DEBUG DB ROW:", row)

    yield {
        "id_externo": id_externo,
        "codigo_barras": codigo,
        "nombre": nombre,
    }

    # teardown: borrar el producto creado
    cur.execute("DELETE FROM productos WHERE id_externo = %s", (id_externo,))
    db_conn.commit()
    cur.close()
