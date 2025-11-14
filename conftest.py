import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser():
    chrome_options = Options()

    # Modo headless para CI/CD (GitHub Actions)
    chrome_options.add_argument("--headless=new")  # headless moderno
    chrome_options.add_argument("--window-size=1920,1080")
    
    
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--remote-allow-origins=*")
    chrome_options.add_argument("--disable-features=AcceptCHFrame")

    # IMPORTANTE para Chrome 140+ (evita desconexão do DevTools)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=chrome_options)

    yield driver
    driver.quit()
