import time
import pyautogui
import pytesseract
from PIL import Image
import os

# Configurar o caminho do Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Coordenadas do botão (substitua pelos valores corretos)
botao_x, botao_y = 422, 585

# Coordenadas da área da mensagem (substitua pelos valores corretos)
mensagem_x1, mensagem_y1 = 826, 300  # Ajuste estas coordenadas
mensagem_x2, mensagem_y2 = 994, 318  # Ajuste estas coordenadas

# Texto esperado da mensagem
texto_esperado = "Não há vagas disponíveis."

# Diretório para salvar as imagens
diretorio_imagens = os.path.join(os.getcwd(), 'imagens')
os.makedirs(diretorio_imagens, exist_ok=True)

def clicar_repetidamente(max_repeticoes=2000):
    contador = 0
    while contador < max_repeticoes:
        try:
            # Clicar no botão
            time.sleep(5)
            pyautogui.click(botao_x, botao_y)
            
            # Aguardar 1 segundo
            time.sleep(3)
            
            # Capturar a área da mensagem
            screenshot = pyautogui.screenshot(region=(mensagem_x1, mensagem_y1, mensagem_x2 - mensagem_x1, mensagem_y2 - mensagem_y1))
            
            # Usar OCR para ler o texto da mensagem com configurações ajustadas
            custom_config = r'--oem 3 --psm 6'
            mensagem = pytesseract.image_to_string(screenshot, lang='por', config=custom_config).strip()
            
            # Imprimir a mensagem capturada para depuração
            print(f"Mensagem capturada: '{mensagem}'")
            
            # Se o texto da mensagem for diferente do esperado, capturar a tela inteira e salvar a imagem
            if mensagem != texto_esperado:
                print("Mensagem diferente encontrada:", mensagem)
                screenshot_full = pyautogui.screenshot()
                screenshot_full.save(os.path.join(diretorio_imagens, f'mensagem_diferente_{contador}.png'))
                break
            
            contador += 1
        
        except Exception as e:
            print("Erro:", e)
            break
    
    if contador >= max_repeticoes:
        print("Limite máximo de repetições atingido.")

# Chamar a função para iniciar o processo com um limite de 20 repetições
clicar_repetidamente(max_repeticoes=2000)
