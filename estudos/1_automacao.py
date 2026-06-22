import pyautogui as posicaoMouse

# Aguardar tempo
posicaoMouse.sleep(2)

# Mover para a posição... (Botão windows)
posicaoMouse.moveTo(x=693, y=1049)
#Clicar na posição... (Botão windows)
posicaoMouse.click(x=693, y=1049)

posicaoMouse.sleep(4)

# Exibir a posição do mouse 
#print(posicaoMouse.position())

# Clicar na posição... (Botão calculadora)
posicaoMouse.moveTo(x=1031, y=540)
# Clicar na posição... (Botão calculadora)
posicaoMouse.click(x=1031, y=540)