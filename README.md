# 🧪 Automação de Testes com Selenium – Bikcraft  
Automação completa do site **Bikcraft** utilizando **Python + Selenium WebDriver + Pytest**, seguindo padrões profissionais adotados por equipes de QA Sênior.

Este projeto faz parte do meu portfólio e demonstra habilidades reais em automação de UI, arquitetura POM, cenários complexos e boas práticas modernas de QA.

---

## 🚀 Tecnologias Utilizadas
- **Python 3.10+**
- **Selenium WebDriver**
- **Pytest**
- **Pytest-HTML**
- **WebDriver Manager**
- **Page Object Model (POM)**

---

## 🎯 Objetivo do Projeto

Este repositório tem como propósito demonstrar experiência profissional em:

- Estruturar projetos de automação de forma escalável  
- Criar Page Objects limpos, reutilizáveis e de fácil manutenção  
- Automatizar cenários reais de UI  
- Utilizar seletores estáveis e eficientes  
- Validar navegação, formulários, mensagens e comportamentos  
- Gerar relatórios HTML profissionais via Pytest  

---

## 📂 Estrutura do Projeto
```
selenium_python/
│
├── pages/ # Page Objects
│ ├── home_page.py
│ ├── contato_page.py
│ ├── seguros_page.py
│ ├── bicicletas_page.py
│
├── tests/ # Suíte de testes
│ ├── test_navegacao_contato.py
│ ├── test_navegacao_seguro.py
│ ├── test_navegacao_bicicleta.py
│ 
├── conftest.py # Setup global (WebDriver, fixtures)
├── requirements.txt # Dependências
└── README.md

```

---

# 🧱 Arquitetura – Page Object Model (POM)

O projeto segue rigorosamente o padrão **POM**, garantindo:

✓ Código limpo e desacoplado  
✓ Alta manutenibilidade  
✓ Reutilização de seletores e métodos  
✓ Testes curtos, focados apenas na lógica de validação  
✓ Estrutura escalável para projetos grandes  

---

# 📝 Cenários Automatizados

## ✔ **1. Navegação até Contato**
- Acessa a home  
- Clica no menu **Contato**  
- Valida se a página carregou corretamente  

Arquivo:  
`tests/test_navegacao_contato.py`

---

## ✔ **2. Envio do Formulário de Contato**
- Preenche todos os campos  
- Envia o formulário  
- Valida a mensagem de erro:

> *"Erro no envio, você pode enviar diretamente para o nosso email em: contato@bikcraft.net"*  

Arquivo:  
`tests/test_form_contato.py`

---

## ✔ **3. Navegação e teste do fluxo de Seguros**
- Acessa o menu **Seguros**  
- Clica no plano **Ouro**  
- Preenche todo o formulário  
- Valida retorno esperado  

Arquivo:  
`tests/test_navegacao_seguro.py`

---

## ✔ **4. Teste completo de Bicicletas – fluxo real**
- Clica no menu **Bicicletas**  
- Seleciona **Mais Sobre** da primeira bike  
- Valida carregamento da página da bike  
- Clica em **Comprar agora**  
- Preenche o formulário de orçamento  
- Seleciona o tipo **Bikcraft**  
- Submete o formulário e valida resposta  

Arquivo:  
`tests/test_navegacao_bicicleta.py`

---

# ⚙️ Como Executar o Projeto

### 1️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```
### 2️⃣ Executar todos os testes
```
pytest -v
```

### 3️⃣ Executar um teste específico
```
pytest tests/test_navegacao_bicicleta.py -v
```

### 4️⃣ Gerar relatório HTML
```
pytest --html=report.html --self-contained-html
```
O arquivo report.html será gerado na raiz do projeto.

## 🧩 Setup Selenium explicado

O conftest.py garante um setup profissional:

   - WebDriver configurado automaticamente

   - Chrome iniciado em modo maximizado

   - Evita erros de sandbox e GPU

   - Finaliza o driver ao término dos testes

   - Reutilizável por toda a suíte

## 🏆 Destaques Técnicos

✔ Arquitetura POM profissional

✔ Page Objects claros e reutilizáveis

✔ Localizadores estáveis (CSS e XPath otimizados)

✔ Uso avançado de WebDriverWait + Expected Conditions

✔ Boas práticas de QA Sênior

✔ Estrutura modular, escalável e organizada

✔ Relatórios HTML profissionais

✔ Projeto fácil de rodar em qualquer máquina


## 👨‍💻 Autor

Talisson Werley - 
Analista de QA 


🔗 LinkedIn:
https://www.linkedin.com/in/talissonwerley
