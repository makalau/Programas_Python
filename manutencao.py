from os import system
import sys

commands = {1:"sfc /scannow", 2:"taskmgr", 3:"chkdisk", 4:"cleanmgr", 5:"ipconfig/flushdns", 6:"exit"} 

def windows():
    print("Bem vindo ao software de manutenção do windows")
    print()
    print("[ 1 ] WFP         [ 2 ] Task Manager  [ 3 ] Disk Scan   \n[ 4 ] Clean Disk  [ 5 ]Clean DNS      [ 6 ] Sair")
    while True:
        choice = int(input("Digite o comando: "))
        continua = str(input("Deseja continuar[S/N]: ").lower().strip())
        if continua == 'n':
            break
        system(commands[choice])

try:
    windows()
except KeyboardInterrupt:
    system("cls")
    print("Programa encerrado com sucesso!!")