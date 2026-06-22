import pyautogui as posicaoMouse   

posicaoMouse.sleep(2)
#print(posicaoMouse.position())

posicaoMouse.moveTo(x=42, y=192)
posicaoMouse.doubleClick(x=42, y=192)

posicaoMouse.sleep(5)

posicaoMouse.typewrite('https://www.google.com/')

posicaoMouse.sleep(2)

#Selecionar e executar uma tecla 
posicaoMouse.press('enter')

posicaoMouse.sleep(2)

posicaoMouse.typewrite('Dolar hoje')
posicaoMouse.sleep(2)
posicaoMouse.press('enter')


