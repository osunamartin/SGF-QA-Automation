from utils.db import get_db_connection

def test_db_has_products():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM productos;")
    count = cur.fetchone()[0]

    cur.close()
    conn.close()

    assert count > 0, "La tabla productos está vacía. No se cargaron productos."
