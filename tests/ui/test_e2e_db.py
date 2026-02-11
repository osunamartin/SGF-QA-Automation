import os
from dotenv import load_dotenv
from playwright.sync_api import expect

load_dotenv()

#Carga un producto en la base de datos y lo busca, lo borra al final del test. (Prueba de productos dinámicos)
def test_e2e_product_created_in_db_is_visible_in_ui(page, test_product):
    base_url = os.getenv("BASE_URL", "http://localhost:3000")
    page.goto(base_url)

    search = page.get_by_role("textbox", name="Escanee código o escriba...")
    expect(search).to_be_visible()

    search.click()
    search.fill(test_product["nombre"])
    search.press("Enter")
    page.wait_for_timeout(500)

    expect(page.get_by_text(test_product["nombre"])).to_be_visible()
    expect(page.get_by_text(test_product["codigo_barras"])).to_be_visible()

    page.wait_for_timeout(500)

    expect(page.get_by_text(test_product["nombre"])).to_be_visible()
