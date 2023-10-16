import pyautogui
import time

#esperar a cada comando
pyautogui.PAUSE = 2
# Abrir o programa
pyautogui.press("win")
pyautogui.write('login.xlsx')
pyautogui.press("backspace")
pyautogui.press("Enter")

# Preencher o login
pyautogui.click(426, 282)
pyautogui.write('igor')

# Preencher a senha
pyautogui.click(394, 328)
pyautogui.write('123')

# Clicar em fazer login
pyautogui.click(364, 433)

# pegar a posição do mouse
'''
time.sleep(3)
position = pyautogui.position()
print(position)
'''

# 426, 282
# 394, 328
# 364, 433
