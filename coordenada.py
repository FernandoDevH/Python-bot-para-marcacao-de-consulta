
import pyautogui
import time

# Timer de 3 segundos para posicionar o mouse
print("Posicione o mouse no local desejado em 3 segundos...")
time.sleep(3)

# Capturar as coordenadas do mouse
x, y = pyautogui.position()

print(f"As coordenadas do mouse são: X={x}, Y={y}")
