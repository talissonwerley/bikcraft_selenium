from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContatoPage:

    def __init__(self, driver):
        self.driver = driver

    # Campos do formulário
    nome = (By.ID, "nome")
    email = (By.ID, "email")
    telefone = (By.ID, "telefone")
    mensagem = (By.ID, "mensagem")

    # Botão
    botao_enviar = (By.CSS_SELECTOR, "button.botao.col-2")

    # Mensagem de erro
    mensagem_erro = (By.CSS_SELECTOR, "section.contato-formulario form p")

    def preencher_nome(self, valor):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.nome)
        ).send_keys(valor)

    def preencher_email(self, valor):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.email)
        ).send_keys(valor)

    def preencher_telefone(self, valor):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.telefone)
        ).send_keys(valor)

    def preencher_mensagem(self, valor):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.mensagem)
        ).send_keys(valor)

    def clicar_enviar(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.botao_enviar)
        ).click()

    def validar_mensagem_erro(self):
        texto_esperado = "Erro no envio, você pode enviar diretamente para o nosso email em: contato@bikcraft.net"

        elemento = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.mensagem_erro)
        )

        return texto_esperado in elemento.text
