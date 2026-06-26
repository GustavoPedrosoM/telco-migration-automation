import os
from navegador import (
    iniciar_driver, aguardar_login_manual,
    acessar_migracao, clicar_novo,
    acessar_relatorios_migracao, acessar_erro,
    ordenar_migracao_descendente,
    executar_migracao )
from upload import preencher_migracao, clicar_salvar, mover_para_feito
from log_checker import verificar_erros_relatorio
from dotenv import load_dotenv

load_dotenv()

driver = iniciar_driver()
aguardar_login_manual(driver)
acessar_migracao(driver)

while True:
    clicar_novo(driver)
    caminho = preencher_migracao(driver)

    if not caminho:
        print("Sem arquivos para processar")
        break

    clicar_salvar(driver) 
    acessar_relatorios_migracao(driver)
    acessar_erro(driver)
    sem_erros = verificar_erros_relatorio(driver)

    if not sem_erros:
        driver.quit()
        exit()
    
    mover_para_feito(caminho)
    acessar_migracao(driver)
    ordenar_migracao_descendente(driver)
    executar_migracao(driver)

input("Pressione ENTER para fechar...")
driver.quit()