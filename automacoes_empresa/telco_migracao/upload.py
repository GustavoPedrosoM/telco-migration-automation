from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path


def obter_proximo_arquivo():
    home = Path.home()
    for nome_pasta in ["Documents", "Documentos"]:
        pasta = home / nome_pasta / "Enderecos"
        if pasta.exists():
            arquivos = sorted(pasta.glob("*.xlsx"))
            if arquivos:
                return str(arquivos[0])

    return None


def preencher_migracao(driver):
    espera = WebDriverWait(driver, 15)

    # ======================
    # Tipo migração
    # ======================

    tipo = espera.until(
        EC.presence_of_element_located(
            (By.NAME, "identificadorTipoMigracao")
        )
    )

    Select(tipo).select_by_visible_text("Endereco Terceiros")

    # ======================
    # Ambiente
    # ======================

    ambiente = espera.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "select[ng-model='migracaoDados.ambienteMigracao']")
        )
    )

    Select(ambiente).select_by_visible_text("HOMOLOGACAO")

    # ======================
    # Arquivo automático
    # ======================

    caminho = obter_proximo_arquivo()

    if not caminho:
        print("Nenhum arquivo encontrado")
        return False

    print(f"Enviando: {caminho}")

    upload = espera.until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@type='file']")
        )
    )

    upload.send_keys(caminho)

    # ======================
    # Ação
    # ======================

    acao = espera.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "select[ng-model='migracaoDados.acao']")  # ajuste o ng-model correto
        )
    )

    Select(acao).select_by_visible_text("ANALISE")

    return True

def clicar_salvar(driver):
    espera = WebDriverWait(driver, 15)

    salvar = espera.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type='submit'].btn.btn-primary")
        )
    )

    salvar.click()