import pytest
from pages.home_page import HomePage
from pages.bicicletas_page import BicicletasPage
import time

def test_comprar_primeira_bike(browser):
    home = HomePage(browser)
    bike = BicicletasPage(browser)

    # 1. Abrir página inicial
    home.abrir()

    # 2. Clicar no menu "Bicicletas"
    home.clicar_menu_bicicletas()  # vamos criar essa função no HomePage

    # 3. Clicar em "MAIS SOBRE" da primeira bike
    bike.clicar_primeira_bike()

    # 4. Checar se página da bicicleta está visível
    assert bike.verificar_pagina_bike_visivel(), "Página da bicicleta não apareceu"

    # 5. Clicar em "Comprar Agora"
    bike.clicar_comprar_agora()
