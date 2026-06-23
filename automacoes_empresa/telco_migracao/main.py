from navegador import (
    iniciar_driver, fazer_login,
    acessar_migracao, clicar_novo
)
from upload import preencher_migracao, clicar_salvar

driver = iniciar_driver()

fazer_login(driver, "gustavo.machado", "@Tfttop8")

acessar_migracao(driver)
clicar_novo(driver)

ok = preencher_migracao(driver)

if not ok:
    print("Sem arquivos para processar")
else:
    clicar_salvar(driver)
    acessar_migracao(driver)  # aguarda o carregamento e volta para a tela

input("Pressione ENTER para fechar...")
driver.quit()