from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import tkinter as tk 
from tkinter import messagebox

def verificar_erros_relatorio(driver):

    espera = WebDriverWait(driver, 15)

    espera.until(
        lambda d: len(d.window_handles) > 1
    )

    driver.switch_to.window(driver.window_handles[-1])

    espera.until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    tabelas = driver.find_elements(By.CLASS_NAME, "jrPage")

    if tabelas:
        # cria janela tkinter oculta (necessário para o messagebox funcionar)
        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)  # força em primeiro plano
        root.focus_force()

        messagebox.showerror(
            title="Erro na Planilha",
            message="⚠️ Foram encontrados erros na planilha!\n\nCorreja o arquivo e execute o script novamente."
        )

        root.destroy()
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        return False

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    return True