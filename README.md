📌 TELCO MIGRATION AUTOMATION

Automação em Python para execução e validação de migrações em massa no sistema Telco.

────────────────────────────────────────────

🎯 OBJETIVO

Automatizar etapas manuais do processo de migração de dados, reduzindo tempo operacional e minimizando erros durante execuções repetitivas.

────────────────────────────────────────────

⚙️ FLUXO AUTOMATIZADO

• Acesso ao sistema Telco

• Login automático

• Navegação até tela de migração

• Seleção de parâmetros

• Upload de arquivos

• Execução da análise

• Verificação de logs e erros

• Execução final da migração

────────────────────────────────────────────

🧰 TECNOLOGIAS UTILIZADAS

• Python 3.x

• Selenium

• Chrome WebDriver

• python-dotenv

────────────────────────────────────────────

📁 ESTRUTURA DO PROJETO

telco_migracao/

* main.py
* navegador.py
* upload.py
* log_checker.py
* .env.example
* .gitignore
* requirements.txt

────────────────────────────────────────────

⚙️ CONFIGURAÇÃO DO AMBIENTE

Este projeto utiliza variáveis de ambiente para proteger informações sensíveis como credenciais e URLs.

────────────────────────────

1. Criar arquivo .env

Na raiz do projeto, criar um arquivo chamado .env:

TELCO_URL=[https://teste.adapter.net.br/adapter/#/login](https://teste.adapter.net.br/adapter/#/login)

TELCO_USER=seu_usuario

TELCO_PASSWORD=sua_senha

🔐 Importante:

• O arquivo .env contém dados sensíveis

• NÃO deve ser enviado ao GitHub

• Já está incluído no .gitignore

────────────────────────────

2. Exemplo de arquivo .env.example

TELCO_URL=

TELCO_USER=

TELCO_PASSWORD=

────────────────────────────────────────────

📦 INSTALAÇÃO

1. Criar ambiente virtual (opcional, recomendado)

Windows:

python -m venv venv

venv\Scripts\activate

Linux / Mac:

source venv/bin/activate

────────────────────────────

2. Instalar dependências

pip install -r requirements.txt

ou

pip install selenium python-dotenv

────────────────────────────────────────────

🚀 COMO EXECUTAR

Após configurar o .env:

python main.py

────────────────────────────────────────────

🔄 COMO FUNCIONA O USO DO .env

O projeto carrega automaticamente as variáveis de ambiente:

import os

from dotenv import load_dotenv

load_dotenv()

usuario = os.getenv("TELCO_USER")

senha = os.getenv("TELCO_PASSWORD")

url = os.getenv("TELCO_URL")

────────────────────────────────────────────

👥 USO EM MÚLTIPLOS AMBIENTES

🧪 Homologação:

TELCO_URL=[https://teste.adapter.net.br/adapter/#/login](https://teste.adapter.net.br/adapter/#/login)

TELCO_USER=usuario_teste

TELCO_PASSWORD=senha_teste

🚀 Produção:

TELCO_URL=[https://producao.adapter.net.br/adapter/#/login](https://producao.adapter.net.br/adapter/#/login)

TELCO_USER=usuario_real

TELCO_PASSWORD=senha_real

────────────────────────────────────────────

🔒 BOAS PRÁTICAS

• Nunca commitar o arquivo .env

• Usar sempre .env.example como base

• Cada desenvolvedor deve ter seu próprio .env

• Não armazenar credenciais no código

• Separar ambientes (produção / homologação)

────────────────────────────────────────────

🧪 PRIMEIRA EXECUÇÃO

1. Clonar o repositório
2. Criar arquivo .env
3. Instalar dependências
4. Executar: python main.py

────────────────────────────────────────────

📌 OBSERVAÇÕES FINAIS

• O projeto utiliza Selenium para automação de navegador

• O ChromeDriver deve ser compatível com a versão do Chrome instalada

• O funcionamento depende da disponibilidade do sistema Telco

────────────────────────────────────────────
