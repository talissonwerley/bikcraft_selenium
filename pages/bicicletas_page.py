from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BicicletasPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Botão "Mais Sobre" da primeira bike (Nimbus)
    BTN_MAIS_SOBRE_PRIMEIRA_BIKE = (
        By.CSS_SELECTOR, "a.botao.seta[href='./bicicletas/nimbus.html']"
    )

    # Título da página da bike (validar se está visível)
    TITULO_BIKE = (
        By.XPATH, "//h1[contains(text(), 'Nimbus Stark')]"
    )

    # Botão "Comprar Agora"
    BTN_COMPRAR_AGORA = (
        By.XPATH, "//a[contains(text(), 'Comprar Agora')]"
    )


    # ======== AÇÕES =========

    def clicar_primeira_bike(self):
        btn = self.wait.until(
            EC.element_to_be_clickable(self.BTN_MAIS_SOBRE_PRIMEIRA_BIKE)
        )
        btn.click()
        time.sleep(1)

    def verificar_pagina_bike_visivel(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.TITULO_BIKE))
            return True
        except:
            return False

    def clicar_comprar_agora(self):
        btn = self.wait.until(
            EC.element_to_be_clickable(self.BTN_COMPRAR_AGORA)
        )
        btn.click()
        time.sleep(1)
    