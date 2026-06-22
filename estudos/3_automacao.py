import pyautogui as abrirArquivos

# Permite executar mais de uma tecla de atalho
abrirArquivos.hotkey('win', 'r')

abrirArquivos.sleep(2)
abrirArquivos.typewrite('notepad')
abrirArquivos.press('enter')

abrirArquivos.sleep(2)
abrirArquivos.typewrite('Abrimos o notepad com um script')

abrirArquivos.sleep(2)
# Permite selecionar a janela que está ativa
fecharJanela = abrirArquivos.getActiveWindow()

abrirArquivos.sleep(2)  
fecharJanela.close()

