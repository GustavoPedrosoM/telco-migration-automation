import time
import os
import subprocess
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

load_dotenv()

def obter_versao_chrome():
    try:
        resultado = subprocess.run(
            r'reg query "HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon" /v version',
            capture_output=True, text=True, shell=True
        )
        versao = re.search(r'(\d+)\.\d+\.\d+\.\d+', resultado.stdout)
        if versao:
            return versao.group(1)
    except:
        pass
    return None

def iniciar_driver():
    url = os.getenv("TELCO_URL")
    versao = obter_versao_chrome()
    service = Service(ChromeDriverManager(driver_version=versao).install())
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    driver.maximize_window()
    return driver


def aguardar_login_manual(driver):
    espera = WebDriverWait(driver, 300)

    espera.until(
        EC.url_contains("/adapter/#/home")
    )


def acessar_migracao(driver):
    espera = WebDriverWait(driver, 60)

    espera.until(
        EC.invisibility_of_element_located(
            (By.CLASS_NAME, "modal-loading")
        )
    )

    menu_migracao = espera.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(normalize-space(.), 'Migração')]")
        )
    )

    driver.execute_script("arguments[0].click();", menu_migracao)
    time.sleep(1)

    migracao_massa = espera.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(normalize-space(.), 'Migração / Alteração de dados em massa')]")
        )
    )

    driver.execute_script("arguments[0].click();", migracao_massa)


def clicar_novo(driver):
    espera = WebDriverWait(driver, 60)

    aguardar_carregamento(driver)

    botao_novo = espera.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@href='#/migracao/migracao_dados/novo']")
        )
    )

    driver.execute_script("arguments[0].click();", botao_novo)


def acessar_relatorios_migracao(driver):
    espera = WebDriverWait(driver, 60)

    aguardar_carregamento(driver)

    espera.until(
        EC.url_contains("/migracao/migracao_dados")
    )

    menu_migracao = espera.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(normalize-space(.), 'Migração')]")
        )
    )

    driver.execute_script("arguments[0].click();", menu_migracao)

    relatorios = espera.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[href='#/relatorios/migracao']")
        )
    )

    driver.execute_script("arguments[0].click();", relatorios)

    espera.until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[@href='#/relatorios/migracao/42']")
        )
    )


def acessar_erro(driver):
    espera = WebDriverWait(driver, 60)

    botao_erro = espera.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@href='#/relatorios/migracao/42']")
        )
    )

    driver.execute_script("arguments[0].click();", botao_erro)

    botao_visualizar = espera.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(normalize-space(.), 'Visualizar')]")
        )
    )

    driver.execute_script("arguments[0].click();", botao_visualizar)

    time.sleep(4)

    espera.until(
        lambda d: len(d.window_handles) > 1
    )


def ordenar_migracao_descendente(driver):
    espera = WebDriverWait(driver, 30)

    th_numero = espera.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "th.hidden-xs[aria-controls='viewMigracaoDados']")
        )
    )

    if "sorting_desc" not in th_numero.get_attribute("class"):
        driver.execute_script("arguments[0].click();", th_numero)

    espera.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "th.hidden-xs.sorting_desc[aria-controls='viewMigracaoDados']")
        )
    )


def executar_migracao(driver):
    espera = WebDriverWait(driver, 30)

    botao_executar = espera.until(
        EC.element_to_be_clickable(
            (By.XPATH, "(//button[@ng-click='migrarAnalise(migracaoDados)'])[1]")
        )
    )

    driver.execute_script("arguments[0].click();", botao_executar)

    botao_ok = espera.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@data-bb-handler='confirm']")
        )
    )

    botao_ok.click()


def aguardar_carregamento(driver, timeout=60):
    espera = WebDriverWait(driver, timeout)

    espera.until(
        EC.invisibility_of_element_located(
            (By.CLASS_NAME, "loader-text")
        )
    )

    espera.until(
        EC.invisibility_of_element_located(
            (By.CLASS_NAME, "modal-loading")
        )
    )

    time.sleep(6)