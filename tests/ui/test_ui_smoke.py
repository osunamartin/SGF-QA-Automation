import re
from playwright.sync_api import expect


def test_ui_smoke(page):
    # 1) Abrir la app
    page.goto("http://localhost:3000/")

    # 2) Check básico: algo visible que confirme que cargó
    expect(page.get_by_text("¿Búsqueda Avanzada? (F2)")).to_be_visible()

    # 3) Acciones grabadas (Codegen)
    page.get_by_text("¿Búsqueda Avanzada? (F2)").click()
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).click()
    page.get_by_role("textbox", name="Escanee código o escriba...").click()
    page.get_by_role("textbox", name="Escanee código o escriba...").fill("")
    page.get_by_text("F1 Ayuda").click()
    page.get_by_text("F1 AyudaF12 CobrarF2 Buscar").click()
    page.locator("body").press("Escape")
    page.get_by_role("textbox", name="Escanee código o escriba...").press("F1")
    page.get_by_role("textbox", name="Escanee código o escriba...").press("Escape")
    page.get_by_role("textbox", name="Escanee código o escriba...").press("F2")
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).click()
