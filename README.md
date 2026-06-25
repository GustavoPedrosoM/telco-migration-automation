
# Telco Migration Automation

Automação em Python para execução e validação de migrações em massa no sistema Telco.

## Objetivo

Automatizar etapas manuais do processo de migração de dados, reduzindo tempo operacional e minimizando erros durante execuções repetitivas.

Fluxo atual:

- Acesso automático ao sistema
- Login automatizado
- Navegação até tela de migração
- Seleção dos parâmetros da migração
- Upload automático dos arquivos
- Execução da análise
- Verificação de erros
- Execução da migração

## Tecnologias

- Python 3.x
- Selenium
- Chrome WebDriver

## Estrutura do projeto

```plaintext
automacoes_empresa/
└── telco_migracao/
    ├── main.py
    ├── navegador.py
    ├── upload.py
    └── log_checker.py
```

## Como executar

Instalar dependências:

```bash
pip install -r requirements.txt
```

Executar:

```bash
python automacoes_empresa/telco_migracao/main.py
```

## Observações

- O projeto utiliza arquivos locais para processamento.
- Credenciais e arquivos sensíveis não devem ser versionados.
- Configurações específicas de ambiente devem permanecer locais.
