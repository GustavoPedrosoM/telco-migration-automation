📌 TELCO MIGRATION AUTOMATION

Automação em Python para execução e validação de migrações em massa no sistema Telco.

━━━━━━━━━━━━━━━━━━━━━━

🎯 OBJETIVO

━━━━━━━━━━━━━━━━━━━━━━

Automatizar etapas manuais do processo de migração de dados, reduzindo tempo operacional, aumentando a padronização do processo e minimizando erros durante execuções repetitivas.

━━━━━━━━━━━━━━━━━━━━━━

⚙️ VISÃO GERAL — FLUXO AUTOMATIZADO

━━━━━━━━━━━━━━━━━━━━━━

✔️ Acesso ao sistema Telco

✔️ Login manual realizado pelo usuário

✔️ Navegação automática até a tela de migração

✔️ Seleção dos parâmetros necessários

✔️ Upload automático das planilhas

✔️ Execução da análise

✔️ Verificação de logs e validação de erros

✔️ Movimentação das planilhas processadas

✔️ Execução final da migração

━━━━━━━━━━━━━━━━━━━━━━

🧰 TECNOLOGIAS UTILIZADAS

━━━━━━━━━━━━━━━━━━━━━━

• Python 3.x

• Selenium

• Chrome WebDriver

• python-dotenv

━━━━━━━━━━━━━━━━━━━━━━

📁 ESTRUTURA DO PROJETO

━━━━━━━━━━━━━━━━━━━━━━

telco_migracao/

├── main.py

├── navegador.py

├── upload.py

├── log_checker.py

├── .env

├── .env.example

├── .gitignore

└── requirements.txt

━━━━━━━━━━━━━━━━━━━━━━

⚙️ CONFIGURAÇÃO DO AMBIENTE

━━━━━━━━━━━━━━━━━━━━━━

Este projeto utiliza variáveis de ambiente para proteger informações sensíveis, como a URL do sistema.

1️⃣ Criar arquivo .env

Na raiz do projeto, criar um arquivo chamado:

.env

Conteúdo:

TELCO_URL=link_telco

🔐 Importante:

• O arquivo .env contém dados sensíveis

• NÃO deve ser enviado ao GitHub

• Já está incluído no .gitignore

2️⃣ Arquivo de exemplo (.env.example)

Conteúdo:

TELCO_URL=

━━━━━━━━━━━━━━━━━━━━━━

📦 INSTALAÇÃO

━━━━━━━━━━━━━━━━━━━━━━

1️⃣ Criar ambiente virtual (recomendado)

Windows:

python -m venv venv

venv\Scripts\activate

Linux / Mac:

source venv/bin/activate

2️⃣ Instalar dependências

pip install -r requirements.txt

ou

pip install selenium python-dotenv

━━━━━━━━━━━━━━━━━━━━━━

🚀 COMO EXECUTAR

━━━━━━━━━━━━━━━━━━━━━━

▶️ Via Python

Após configurar o arquivo .env:

python main.py

▶️ Via Executável (.exe)

O projeto também pode ser distribuído como executável (.exe) para facilitar o uso por usuários que não possuem ambiente Python configurado.

Regras:

• Executar o arquivo .exe diretamente

• O arquivo .env deve estar na mesma pasta do executável

━━━━━━━━━━━━━━━━━━━━━━

🔑 LOGIN

━━━━━━━━━━━━━━━━━━━━━━

Ao iniciar, o script abre automaticamente o navegador na tela de login do sistema Telco.

O usuário deve:

1. Inserir suas credenciais manualmente
2. Realizar autenticação normalmente

Após o login, a automação detecta a autenticação e assume o controle automaticamente.

✅ Nenhuma credencial é armazenada em arquivos ou no código.

━━━━━━━━━━━━━━━━━━━━━━

👥 USO EM MÚLTIPLOS AMBIENTES

━━━━━━━━━━━━━━━━━━━━━━

🧪 Ambiente de Homologação

TELCO_URL=

🚀 Ambiente de Produção

TELCO_URL=

Cada usuário pode configurar seu próprio ambiente apenas alterando o arquivo .env.

━━━━━━━━━━━━━━━━━━━━━━

🔒 BOAS PRÁTICAS

━━━━━━━━━━━━━━━━━━━━━━

✅ Nunca commitar o arquivo .env

✅ Utilizar .env.example como modelo

✅ Cada usuário deve possuir seu próprio .env

✅ Não armazenar credenciais no código

✅ Separar ambientes de homologação e produção

✅ Utilizar controle de versão no projeto

━━━━━━━━━━━━━━━━━━━━━━

🧪 PRIMEIRA EXECUÇÃO

━━━━━━━━━━━━━━━━━━━━━━

1. Clonar o repositório
2. Criar arquivo .env com a URL do sistema
3. Instalar dependências
4. Executar:

python main.py

5. Realizar login manual no navegador aberto
6. Aguardar a automação assumir o processo

━━━━━━━━━━━━━━━━━━━━━━

📂 PROCESSO DE ENTRADA DE ARQUIVOS (PLANILHAS)

━━━━━━━━━━━━━━━━━━━━━━

A automação processa planilhas de endereços organizadas localmente no computador.

📥 Origem das Planilhas

As planilhas devem ser baixadas a partir do SharePoint da empresa.

Após o download:

1. Acessar a pasta Documentos
2. Criar uma pasta chamada:

Enderecos

3. Colocar todas as planilhas .xlsx dentro dela

Estrutura esperada:

Documentos/

└── Enderecos/

  ├── arquivo1.xlsx

  ├── arquivo2.xlsx

  └── arquivo3.xlsx

━━━━━━━━━━━━━━━━━━━━━━

🚀 PROCESSAMENTO AUTOMÁTICO DAS PLANILHAS

━━━━━━━━━━━━━━━━━━━━━━

Durante a execução:

• O sistema acessa automaticamente Documentos/Enderecos

• Processa os arquivos um por vez

• Executa análise e validação

• Concluindo com sucesso → move o arquivo para "feito"

• Cria a pasta "feito" automaticamente caso não exista

• Finaliza quando não houver mais arquivos pendentes

Estrutura após execução:

Documentos/

└── Enderecos/

  ├── feito/

  │ ├── arquivo1.xlsx

  │ └── arquivo2.xlsx

  └── arquivo3.xlsx ← arquivo com erro aguardando correção

━━━━━━━━━━━━━━━━━━━━━━

⚠️ TRATAMENTO DE ERROS NAS PLANILHAS

━━━━━━━━━━━━━━━━━━━━━━

Durante o processamento podem ocorrer inconsistências ou falhas de validação.

Quando isso acontecer:

❌ O erro é identificado automaticamente

❌ Um alerta é exibido ao usuário

❌ A planilha permanece na pasta Enderecos

❌ O usuário confirma o alerta

❌ O script é encerrado automaticamente

━━━━━━━━━━━━━━━━━━━━━━

🔧 FLUXO DE CORREÇÃO

━━━━━━━━━━━━━━━━━━━━━━

1. O alerta de erro é exibido
2. O usuário confirma a mensagem
3. O script encerra
4. A planilha é corrigida manualmente
5. O processo é iniciado novamente

Após correção, apenas os arquivos pendentes serão processados.

━━━━━━━━━━━━━━━━━━━━━━

📌 COMPORTAMENTO GERAL

━━━━━━━━━━━━━━━━━━━━━━

• Processamento sequencial (1 planilha por vez)

• Não existe retomada automática após erro

• Cada execução depende da integridade dos arquivos

• A pasta Enderecos é a fonte única de entrada

• Arquivos concluídos são movidos para Enderecos/feito

• Arquivos com erro permanecem para correção

━━━━━━━━━━━━━━━━━━━━━━

📌 OBSERVAÇÕES FINAIS

━━━━━━━━━━━━━━━━━━━━━━

🖥️ O projeto utiliza Selenium para automação de navegador

🌐 O ChromeDriver deve ser compatível com a versão instalada do Chrome

🔄 O funcionamento depende da disponibilidade do sistema Telco

🔒 As credenciais permanecem sob responsabilidade do usuário

🚀 Desenvolvido para reduzir esforço operacional e aumentar confiabilidade em migrações em massa
