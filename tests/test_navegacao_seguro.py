import pytest
from pages.seguros_page import SeguroPage
from pages.home_page import HomePage

import time

def test_envio_form_seguro(browser):
    home = HomePage(browser)
    seguro = SeguroPage(browser)

    # 1. Abrir página inicial
    home.abrir()

    # 2. Clicar no menu "Seguros"
    home.clicar_menu_seguro()  # você pode criar essa função no HomePage

    seguro.clicar_seguro_ouro()
    time.sleep(2)

    # 3. Preencher formulário de seguro
    seguro.preencher_formulario(
        nome="QA Tester",
        sobrenome="Testador",
        cpf="12345678909",
        email="teste@teste.com",
        cep="12345678",
        numero="100",
        logradouro="Rua do Teste",
        bairro="centro",
        cidade="Testolandia",
        estado="TS",
        tipo="seguro",        # conforme parâmetros da URL
        produto="ouro"
    )

    # 4. Clicar em enviar
    seguro.clicar_enviar()

    # 5. Validar mensagem de erro
    assert seguro.mensagem_apareceu(), "Mensagem de erro não apareceu"
