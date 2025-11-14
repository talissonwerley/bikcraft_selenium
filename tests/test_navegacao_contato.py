from pages.home_page import HomePage
from pages.contato_page import ContatoPage

def test_formulario_contato(browser):

    # Instanciar páginas
    home = HomePage(browser)
    contato = ContatoPage(browser)

    # 1. Abrir home
    home.abrir()

    # 2. Ir para Contato
    home.clicar_menu_contato()

    # 3. Preencher todos os campos
    contato.preencher_nome("Talisson QA Tester")
    contato.preencher_email("email@teste.com")
    contato.preencher_telefone("11999999999")
    contato.preencher_mensagem("Mensagem de teste automatizado.")

    # 4. Clicar em Enviar
    contato.clicar_enviar()

    # 5. Validar mensagem de erro esperada
    assert contato.validar_mensagem_erro(), "A mensagem de erro não foi exibida!"
