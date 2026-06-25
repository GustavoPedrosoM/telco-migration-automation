<pre class="overflow-visible! px-0!" data-start="328" data-end="1013"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="relative h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class=""><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0 PDq2pG_selectionAnchorContainer"><code><span># 📌 Telco Migration Automation</span><br/><br/><span>Automação em Python para execução e validação de migrações em massa no sistema Telco.</span><br/><br/><span>---</span><br/><br/><span>## 🎯 Objetivo</span><br/><br/><span>Automatizar etapas manuais do processo de migração de dados, reduzindo tempo operacional e minimizando erros durante execuções repetitivas.</span><br/><br/><span>---</span><br/><br/><span>## ⚙️ Fluxo Automatizado</span><br/><br/><span>- Acesso ao sistema Telco  </span><br/><span>- Login automático  </span><br/><span>- Navegação até tela de migração  </span><br/><span>- Seleção de parâmetros  </span><br/><span>- Upload de arquivos  </span><br/><span>- Execução da análise  </span><br/><span>- Verificação de logs e erros  </span><br/><span>- Execução final da migração  </span><br/><br/><span>---</span><br/><br/><span>## 🧰 Tecnologias Utilizadas</span><br/><br/><span>- Python 3.x  </span><br/><span>- Selenium  </span><br/><span>- Chrome WebDriver  </span><br/><span>- python-dotenv  </span><br/><br/><span>---</span><br/><br/><span>## 📁 Estrutura do Projeto</span><br/></code><span aria-hidden="true" class="PDq2pG_selectionAnchor"></span></pre></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></div></div></pre>

telco_migracao/

├── main.py

├── navegador.py

├── upload.py

├── log_checker.py

├── .env.example

├── .gitignore

└── requirements.txt

<pre class="overflow-visible! px-0!" data-start="1145" data-end="1372"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><br/><span>---</span><br/><br/><span>## ⚙️ Configuração do Ambiente</span><br/><br/><span>Este projeto utiliza variáveis de ambiente para proteger informações sensíveis como credenciais e URLs.</span><br/><br/><span>### 🔐 1. Criar arquivo `.env`</span><br/><br/><span>Na raiz do projeto, crie um arquivo `.env`:</span><br/></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

TELCO_URL=[https://teste.adapter.net.br/adapter/#/login](https://teste.adapter.net.br/adapter/#/login)

TELCO_USER=seu_usuario

TELCO_PASSWORD=sua_senha

<pre class="overflow-visible! px-0!" data-start="1476" data-end="1669"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><br/><span>⚠️ Importante:</span><br/><span>- O arquivo `.env` contém dados sensíveis  </span><br/><span>- Ele **não deve ser versionado no GitHub**  </span><br/><span>- Já está incluído no `.gitignore`  </span><br/><br/><span>---</span><br/><br/><span>### 📄 2. Exemplo de `.env.example`</span><br/></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

TELCO_URL=

TELCO_USER=

TELCO_PASSWORD=

<pre class="overflow-visible! px-0!" data-start="1709" data-end="1857"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><br/><span>---</span><br/><br/><span>## 📦 Instalação</span><br/><br/><span>### 1. Criar ambiente virtual (opcional, recomendado)</span><br/><br/><span>**Windows**</span><br/><span>```bash</span><br/><span>python -m venv venv</span><br/><span>venv\Scripts\activate</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

**Linux / Mac**

<pre class="overflow-visible! px-0!" data-start="1875" data-end="1911"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="relative h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class=""><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span class="ͼ10">source</span><span> venv/bin/activate</span></code></pre></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></div></div></pre>

---

### 2. Instalar dependências

<pre class="overflow-visible! px-0!" data-start="1948" data-end="1991"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="relative h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class=""><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>pip install </span><span class="ͼ12">-r</span><span> requirements.txt</span></code></pre></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></div></div></pre>

ou

<pre class="overflow-visible! px-0!" data-start="1997" data-end="2043"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="relative h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class=""><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>pip install selenium python-dotenv</span></code></pre></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></div></div></pre>

---

## 🚀 Como Executar

Após configurar o `.env`:

<pre class="overflow-visible! px-0!" data-start="2098" data-end="2124"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="relative h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class=""><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>python main.py</span></code></pre></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></div></div></pre>

---

## 🔄 Uso do `.env` no Código

<pre class="overflow-visible! px-0!" data-start="2162" data-end="2331"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="relative h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class=""><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span class="ͼv">import</span><span></span><span class="ͼ11">os</span><br/><span class="ͼv">from</span><span></span><span class="ͼ11">dotenv</span><span></span><span class="ͼv">import</span><span></span><span class="ͼ11">load_dotenv</span><br/><br/><span class="ͼ11">load_dotenv</span><span>()</span><br/><br/><span class="ͼ11">usuario</span><span></span><span class="ͼv">=</span><span></span><span class="ͼ11">os</span><span class="ͼv">.</span><span>getenv(</span><span class="ͼz">"TELCO_USER"</span><span>)</span><br/><span class="ͼ11">senha</span><span></span><span class="ͼv">=</span><span></span><span class="ͼ11">os</span><span class="ͼv">.</span><span>getenv(</span><span class="ͼz">"TELCO_PASSWORD"</span><span>)</span><br/><span class="ͼ11">url</span><span></span><span class="ͼv">=</span><span></span><span class="ͼ11">os</span><span class="ͼv">.</span><span>getenv(</span><span class="ͼz">"TELCO_URL"</span><span>)</span></code></pre></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></div></div></pre>

---

## 👥 Uso em Múltiplos Ambientes

### 🧪 Homologação

<pre class="overflow-visible! px-0!" data-start="2392" data-end="2506"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>TELCO_URL=https://teste.adapter.net.br/adapter/#/login</span><br/><span>TELCO_USER=usuario_teste</span><br/><span>TELCO_PASSWORD=senha_teste</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

### 🚀 Produção

<pre class="overflow-visible! px-0!" data-start="2525" data-end="2640"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>TELCO_URL=https://producao.adapter.net.br/adapter/#/login</span><br/><span>TELCO_USER=usuario_real</span><br/><span>TELCO_PASSWORD=senha_real</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

---

## 🔒 Boas Práticas

* Nunca commitar o arquivo `.env`
* Usar sempre `.env.example` como base
* Cada desenvolvedor deve ter seu próprio `.env`
* Não armazenar credenciais no código
* Separar ambientes (produção / homologação)

---

## 🧪 Primeira Execução

1. Clonar o repositório
2. Criar o arquivo `.env`
3. Instalar dependências
4. Executar `python main.py`

---

## 📌 Observações

* O projeto utiliza Selenium para automação de navegador
* O ChromeDriver deve ser compatível com a versão do Chrome instalada
* O funcionamento depende da disponibilidade do sistema Telco
