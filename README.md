
## 🧾 Automatizador de Download de Contra-Cheques – Portal do Servidor (Belém/PA)

Este projeto automatiza o processo de login, navegação e download dos contra-cheques no [Portal do Servidor de Belém/PA](https://sistemas.belem.pa.gov.br/portaldoservidor). Desenvolvido com **Python e Selenium**, o script simula o comportamento humano na navegação do portal, economizando tempo e esforço manual.

### 🚀 Funcionalidades

-   Acessa automaticamente o site do Portal do Servidor
    
-   Realiza login com matrícula e senha
    
-   Navega até a área de Contra-Cheques
    
-   Itera por todos os **anos, meses e contratos** disponíveis
    
-   Gera e baixa todos os contra-cheques disponíveis no sistema
    

### 🛠️ Tecnologias Utilizadas

-   Python 3
    
-   Selenium WebDriver
    
-   Google Chrome + ChromeDriver
    

### 📁 Estrutura

O script está dividido em etapas lógicas:

1.  **Configuração do navegador** com opções para downloads automáticos.
    
2.  **Login automatizado** com matrícula e senha.
    
3.  **Navegação inteligente** com espera dinâmica (`WebDriverWait`).
    
4.  **Coleta e iteração** sobre os dropdowns de ano, mês e contrato.
    
5.  **Download automático** dos PDFs gerados de cada contra-cheque.
    

### ⚙️ Como Usar

1.  Instale os pacotes necessários:
    

bash

CopyEdit

`pip install selenium` 

2.  Altere os seguintes campos no código:
    

python

CopyEdit

`"download.default_directory": r"CAMINHO\PARA\DOWNLOAD" matricula_input.send_keys("SUA_MATRICULA")
senha_input.send_keys("SUA_SENHA")` 

3.  Execute o script:
    

bash

CopyEdit

`python baixar_contracheques.py` 

> ⚠️ É necessário ter o **ChromeDriver** compatível com sua versão do Google Chrome instalado.

### 🧠 O que Aprendi

-   Uso avançado do Selenium para lidar com elementos dinâmicos e carregamentos assíncronos.
    
-   Boas práticas de manipulação de exceções e automatização de tarefas repetitivas.
    
-   Integração com o sistema de arquivos para controle de downloads.
    

### 🤝 Contribuição

Este projeto é parte do meu aprendizado contínuo em **automação de processos** e **engenharia de software aplicada a problemas do mundo real**. Fique à vontade para adaptar ou expandir o código conforme sua necessidade.## 🧾 Automatizador de Download de Contra-Cheques – Portal do Servidor (Belém/PA)

Este projeto automatiza o processo de login, navegação e download dos contra-cheques no [Portal do Servidor de Belém/PA](https://sistemas.belem.pa.gov.br/portaldoservidor). Desenvolvido com **Python e Selenium**, o script simula o comportamento humano na navegação do portal, economizando tempo e esforço manual.

### 🚀 Funcionalidades

-   Acessa automaticamente o site do Portal do Servidor
    
-   Realiza login com matrícula e senha
    
-   Navega até a área de Contra-Cheques
    
-   Itera por todos os **anos, meses e contratos** disponíveis
    
-   Gera e baixa todos os contra-cheques disponíveis no sistema
    

### 🛠️ Tecnologias Utilizadas

-   Python 3
    
-   Selenium WebDriver
    
-   Google Chrome + ChromeDriver
    

### 📁 Estrutura

O script está dividido em etapas lógicas:

1.  **Configuração do navegador** com opções para downloads automáticos.
    
2.  **Login automatizado** com matrícula e senha.
    
3.  **Navegação inteligente** com espera dinâmica (`WebDriverWait`).
    
4.  **Coleta e iteração** sobre os dropdowns de ano, mês e contrato.
    
5.  **Download automático** dos PDFs gerados de cada contra-cheque.
    

### ⚙️ Como Usar

1.  Instale os pacotes necessários:
    

bash

CopyEdit

`pip install selenium` 

2.  Altere os seguintes campos no código:
    

python

CopyEdit

`"download.default_directory": r"CAMINHO\PARA\DOWNLOAD" matricula_input.send_keys("SUA_MATRICULA")
senha_input.send_keys("SUA_SENHA")` 

3.  Execute o script:
    

bash

CopyEdit

`python baixar_contracheques.py` 

> ⚠️ É necessário ter o **ChromeDriver** compatível com sua versão do Google Chrome instalado.

### 🧠 O que Aprendi

-   Uso avançado do Selenium para lidar com elementos dinâmicos e carregamentos assíncronos.
    
-   Boas práticas de manipulação de exceções e automatização de tarefas repetitivas.
    
-   Integração com o sistema de arquivos para controle de downloads.
    

### 🤝 Contribuição

Este projeto é parte do meu aprendizado contínuo em **automação de processos** e **engenharia de software aplicada a problemas do mundo real**. Fique à vontade para adaptar ou expandir o código conforme sua necessidade.
