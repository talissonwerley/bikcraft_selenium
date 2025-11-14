from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

class SeguroPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Seletor do formulário
    NOME = (By.NAME, "nome")
    SOBRENOME = (By.NAME, "sobrenome")
    CPF = (By.NAME, "cpf")
    EMAIL = (By.NAME, "email")
    CEP = (By.NAME, "cep")
    NUMERO = (By.NAME, "numero")
    LOGRADOURO = (By.NAME, "logradouro")
    BAIRRO = (By.NAME, "bairro")
    CIDADE = (By.NAME, "cidade")
    ESTADO = (By.NAME, "estado")
    TIPO_SEGURO = (By.ID, "seguro")  # input radio/checkbox associado ao label
    PRODUTO = (By.NAME, "produto")   # se houver select
    BTN_ENVIAR = (By.CSS_SELECTOR, "form button.botao")
    MSG_ERRO = (By.XPATH, "//p[contains(., 'Erro no envio')]")
    LABEL_SEGURO = (By.CSS_SELECTOR, "#orcamento > main > form > div.orcamento-produto > label:nth-child(5)")
    BTN_OURO = (By.CSS_SELECTOR, "#seguros > main > div.seguros.container > div.seguros-item.fadeInRight.anime > a")

    def clicar_seguro_ouro(self):
        # Espera o botão do seguro Ouro ficar visível
        ouro = self.wait.until(EC.visibility_of_element_located(self.BTN_OURO))
        ouro.click()    


    # Funções de interação
    def selecionar_seguro(self):
        # Espera até que o input esteja presente
        input_seguro = self.wait.until(EC.presence_of_element_located(self.TIPO_SEGURO))

        # Se não estiver selecionado, clica no label
        if not input_seguro.is_selected():
            self.driver.find_element(*self.LABEL_SEGURO).click()

    def preencher_formulario(self, nome,sobrenome, email, cpf, cep, numero, logradouro, bairro, cidade, estado,  tipo, produto):
        self.selecionar_seguro()  # garante que a opção seguro esteja selecionada
        self.wait.until(EC.visibility_of_element_located(self.NOME)).send_keys(nome)
        self.wait.until(EC.visibility_of_element_located(self.SOBRENOME)).send_keys(sobrenome)
        self.wait.until(EC.visibility_of_element_located(self.CPF)).send_keys(cpf)
        self.wait.until(EC.visibility_of_element_located(self.EMAIL)).send_keys(email)
        self.wait.until(EC.visibility_of_element_located(self.CEP)).send_keys(cep)
        self.driver.find_element(*self.NUMERO).send_keys(numero)
        self.driver.find_element(*self.LOGRADOURO).send_keys(logradouro)
        self.driver.find_element(*self.BAIRRO).send_keys(bairro)
        self.driver.find_element(*self.CIDADE).send_keys(cidade)
        self.driver.find_element(*self.ESTADO).send_keys(estado)
        

    def clicar_enviar(self):
        self.driver.find_element(*self.BTN_ENVIAR).click()


    def mensagem_apareceu(self):
        try:
            elemento = self.wait.until(EC.visibility_of_element_located(self.MSG_ERRO))
            return "Erro no envio" in elemento.text
        except:
            return False

    time.sleep(5)
