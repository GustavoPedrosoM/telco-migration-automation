from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def iniciar_driver():
    driver = webdriver.Chrome()
    driver.get("https://teste.adapter.net.br/adapter/#/login")
    driver.maximize_window()
    return driver


def fazer_login(driver, usuario_texto, senha_texto):
    time.sleep(3)

    usuario = driver.find_element(By.XPATH, "//input[@type='text']")
    usuario.click()
    usuario.send_keys(usuario_texto)

    time.sleep(1)

    usuario.send_keys("\ue015")  
    usuario.send_keys("\ue007")  

    time.sleep(2)

    senha = driver.find_element(By.XPATH, "//input[@type='password']")
    senha.send_keys(senha_texto)

    time.sleep(1)

    botao = driver.find_element(By.XPATH, "//button[contains(normalize-space(.), 'Entrar')]")
    botao.click()

    time.sleep(5)

import time

def acessar_migracao(driver):

    espera = WebDriverWait(driver, 60)

    # aguarda o modal de loading sumir
    espera.until(
        EC.invisibility_of_element_located(
            (By.CLASS_NAME, "modal-loading")
        )
    )

    # abre menu Migração
    menu_migracao = espera.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//span[contains(normalize-space(.), 'Migração')]"
            )
        )
    )

    driver.execute_script("arguments[0].click();", menu_migracao)
    time.sleep(1)

    migracao_massa = espera.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//span[contains(normalize-space(.), 'Migração / Alteração de dados em massa')]"
            )
        )
    )

    driver.execute_script("arguments[0].click();", migracao_massa)

def clicar_novo(driver):
    espera = WebDriverWait(driver, 60)

    # aguarda os loaders sumirem após execução da migração
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
    print("✓ redirecionou para migracao_dados")

    menu_migracao = espera.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(normalize-space(.), 'Migração')]")
        )
    )

    driver.execute_script("arguments[0].click();", menu_migracao)
    print("✓ clicou no menu Migração")

    relatorios = espera.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[href='#/relatorios/migracao']")
        )
    )

    driver.execute_script("arguments[0].click();", relatorios)
    print("✓ clicou em Relatórios")

    print(f"URL atual: {driver.current_url}")

    espera.until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[@href='#/relatorios/migracao/42']")
        )
    )
    print("✓ encontrou link erro cadastral")

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

    # aguarda a nova aba abrir
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

    # verifica se já está descendente, se não estiver clica
    if "sorting_desc" not in th_numero.get_attribute("class"):
        driver.execute_script("arguments[0].click();", th_numero)

    # aguarda a tabela reordenar
    espera.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "th.hidden-xs.sorting_desc[aria-controls='viewMigracaoDados']")
        )
    )

def executar_migracao(driver):
    espera = WebDriverWait(driver, 30)

    # pega o botão de executar apenas da primeira linha da tabela
    botao_executar = espera.until(
        EC.element_to_be_clickable(
            (By.XPATH, "(//button[@ng-click='migrarAnalise(migracaoDados)'])[1]")
        )
    )

    driver.execute_script("arguments[0].click();", botao_executar)

    # aguarda o modal de confirmação aparecer
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