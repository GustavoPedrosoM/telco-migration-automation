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

    # campo usuário
    usuario = driver.find_element(By.XPATH, "//input[@type='text']")
    usuario.click()
    usuario.send_keys(usuario_texto)

    time.sleep(1)

    usuario.send_keys("\ue015")  # seta para baixo
    usuario.send_keys("\ue007")  # ENTER

    time.sleep(2)

    # campo senha
    senha = driver.find_element(By.XPATH, "//input[@type='password']")
    senha.send_keys(senha_texto)

    time.sleep(1)

    # botão entrar
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

    # tempo extra de garantia após o modal sumir
    time.sleep(3)

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
    espera = WebDriverWait(driver, 10)
    time.sleep(2)
    
    botao_novo = espera.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//a[@href='#/migracao/migracao_dados/novo']"
            )
        )
    )
    
    botao_novo.click()
    time.sleep(2)