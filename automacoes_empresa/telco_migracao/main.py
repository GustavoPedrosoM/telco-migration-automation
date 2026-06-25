from navegador import (
    iniciar_driver, fazer_login,
    acessar_migracao, clicar_novo,
    acessar_relatorios_migracao, acessar_erro,
    ordenar_migracao_descendente,
    executar_migracao )
from upload import preencher_migracao, clicar_salvar, mover_para_feito
from log_checker import verificar_erros_relatorio

driver = iniciar_driver()
fazer_login(driver, "gustavo.machado", "@Tfttop8")
acessar_migracao(driver)

while True:
    clicar_novo(driver)

    caminho = preencher_migracao(driver)

    if not caminho:
        print("Sem arquivos para processar")
        break

    clicar_salvar(driver)
    mover_para_feito(caminho)  # move após salvar com sucesso
    acessar_relatorios_migracao(driver)
    acessar_erro(driver)
    sem_erros = verificar_erros_relatorio(driver)

    if not sem_erros:
        driver.quit()
        exit()

    acessar_migracao(driver)
    ordenar_migracao_descendente(driver)
    executar_migracao(driver)
    # volta para o topo do loop, aguarda carregamento e clica em Novo

input("Pressione ENTER para fechar...")
driver.quit()