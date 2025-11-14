# 🧪 Automação de Testes – Bikcraft  
Testes automatizados para o site **Bikcraft** utilizando **Python, Selenium WebDriver, Pytest e Pytest-HTML**.  
Este projeto foi desenvolvido com foco profissional, seguindo padrões de mercado como **Page Object Model (POM)**, testes modulares, seletores estáveis e boas práticas de QA Sênior.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.10+**
- **Selenium WebDriver**
- **Pytest**
- **Pytest-HTML Reporter**
- **WebDriver Manager**
- **Page Object Model (POM)** como arquitetura base

---

## 📌 Objetivo do Projeto

Este projeto faz parte do meu portfólio profissional como Analista de QA.  
O objetivo é demonstrar minha capacidade em:

- Estruturar testes com qualidade e organização
- Automatizar cenários reais de UI
- Criar Page Objects reutilizáveis e limpos
- Implementar seletores estáveis
- Validar mensagens, redirecionamentos e interações
- Utilizar Pytest com relatórios HTML profissionais

---

## 📂 Estrutura do Projeto

```bash
selenium_python/
│
├── pages/                 # Páginas do POM
│   ├── home_page.py
│   ├── contato_page.py
│
├── tests/                 # Suíte de testes
│   ├── test_navegacao_contato.py
│   ├── test_form_contato.py
│
├── conftest.py            # Fixtures globais do Pytest (setup/teardown do driver)
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação do projeto 
```

## 🧱 Arquitetura – Page Object Model (POM)

O projeto foi construído utilizando o padrão POM (Page Object Model).
Isso garante:

   - Código mais limpo

   - Alta manutenibilidade

   - Separação entre lógica dos testes e lógica das páginas

   - Reuso de métodos e seletores

   - Fluxo profissional usado por equipes de QA automatizado

## 📝 Cenários Automatizados
### ✔ Teste 1 – Navegação até a página de Contato

   - Acessa a home

   - Clica no menu "Contato"

   - Valida se a navegação foi concluída com sucesso

Local do teste:
```
tests/test_navegacao_contato.py
```

## ✔ Teste 2 – Envio do Formulário de Contato

   - Preenche todos os campos do formulário

   - Clica no botão “Enviar Mensagem”

   - Valida se a mensagem de erro aparece corretamente:

``` 
"Erro no envio, você pode enviar diretamente para o nosso email em: contato@bikcraft.net"
```

Local do teste:

```
tests/test_form_contato.py
```

## ⚙️ Como Executar o Projeto
### 1️⃣ Instalar dependências
```
pip install -r requirements.txt
```

### 2️⃣ Executar todos os testes

```
pytest -v
```

### 3️⃣ Executar um teste específico

```
pytest tests/test_form_contato.py -v
```

### 4️⃣ Gerar relatório HTML

```
pytest --html=report.html --self-contained-html
```

O arquivo será gerado na raiz do projeto.

### 🧩 Como Funciona o Setup do Selenium

O conftest.py contém:

   - Inicialização automática do Selenium

   - Resolução automática do ChromeDriver via WebDriver Manager

   - Abas abertas em modo maximizado

   - Fechamento automático ao final dos testes

Isso mantém os testes limpos e reutilizáveis.

### 🏆 Destaques Técnicos

   #### 🧩 POM bem organizado

   #### 🔎 Localizadores estáveis (CSS + XPATH otimizados)

   #### ⏳ Uso de WebDriverWait com Expected Conditions

   ##### 📄 Asserções claras e confiáveis

   #### 📁 Estrutura escalável para múltiplas suítes

   #### 📊 Suporte a relatórios HTML profissionais

   #### 🎯 Testes reproduzíveis em qualquer ambiente

## 👨‍💻 Autor

#### Talisson Werley
Analista de QA | Automação de Testes | Python | Selenium | Pytest

LinkedIn: https://www.linkedin.com/in/talissonwerley
