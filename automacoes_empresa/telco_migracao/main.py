import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv
from navegador import (
    iniciar_driver, aguardar_login_manual,
    acessar_migracao, clicar_novo,
    acessar_relatorios_migracao, acessar_erro,
    ordenar_migracao_descendente,
    executar_migracao
)
from upload import preencher_migracao, clicar_salvar, mover_para_feito
from log_checker import verificar_erros_relatorio

load_dotenv()


def popup_info(titulo, mensagem):
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    messagebox.showinfo(titulo, mensagem)
    root.destroy()


driver = iniciar_driver()
aguardar_login_manual(driver)
acessar_migracao(driver)

while True:
    clicar_novo(driver)
    caminho = preencher_migracao(driver)

    if not caminho:
        popup_info(
            "Concluído",
            "Não há arquivos para processar na pasta Enderecos.\n\nO script será encerrado."
        )
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

popup_info("Concluído", "Todas as planilhas foram processadas com sucesso!")
driver.quit()