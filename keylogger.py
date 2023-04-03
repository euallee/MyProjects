from pynput.keyboard import Listener
import re

def capturar(tecla):
    tecla =  str(tecla)
    tecla = re.sub(r'\'','', tecla)
    print(tecla)

with Listener(on_press=capturar) as l:
    l.join()