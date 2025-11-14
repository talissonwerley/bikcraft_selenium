from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

class HomePage:
    URL = "https://bikcraft-gamma.vercel.app/"

    def __init__(self, driver):
        self.driver = driver

    def abrir(self):
        self.driver.get(self.URL)

    def clicar_menu_contato(self):
        wait = WebDriverWait(self.driver, 10)

        contato_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Contato')]"))
        )
        contato_link.click()
        time.sleep(2)
    
    def clicar_menu_seguro(self):
        wait = WebDriverWait(self.driver, 10)

        # Localiza o link "Seguros" no menu superior
        seguro_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Seguros')]"))
        )
        seguro_link.click()
        time.sleep(2)

    def clicar_menu_bicicletas(self):
        wait = WebDriverWait(self.driver, 10)
        link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Bicicletas')]")))
        link.click()
        time.sleep(2)
