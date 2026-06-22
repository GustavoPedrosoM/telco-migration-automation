from navegador import (
    iniciar_driver,
    fazer_login,
    acessar_migracao,
    clicar_novo
)

# 1. inicia navegador e abre sistema
driver = iniciar_driver()

# 2. faz login
fazer_login(driver, "gustavo.machado", "@Tfttop8")

acessar_migracao(driver)

clicar_novo(driver)

input("Pressione ENTER para fechar...")

driver.quit()