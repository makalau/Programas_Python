import requests
import socket
from os import system
import platform
from time import sleep
from texto import text

def inicio():
    try:
        while True:
            system("cls" if "Win" in platform.system() else "clear")
            text.marca("Bem vindo ao programa")
            text.title('[ 1 ] Consultar IP    [ 2 ] Consulta HostName')
            resp = str(input('Digite: ').strip())
            while not resp or resp not in "12":
                text.erro('Não entendi! Digite uma das opções válidas "1" ou "2"')
                resp = str(input('Digite: ').strip())
            if resp == '1':
                ip = input('Digite o IP que deseja consultar: ').strip()
            else:
                hostname = str(input('Digite o Hostname que deseja consultar: ').strip())
                ip = socket.gethostbyname(hostname)
            url = f"https://api.ipgeolocation.io/ipgeo?apiKey=56c077eec32b46f6839ca726739fba28&ip={ip}&excludes=currency,time_zone"
            result = requests.get(url).json()
            if "not supported" in result['message']:
                print()
                text.erro('IP inválido! confirme-o e tente novamente')
            else:
                for key, value in result.items():
                    print('-'*66)
                    print(f'{key:^15}| {value:>25}')
                print('-'*66)
            continua = str(input('Deseja continuar?[S/N]: ').strip().lower())
            while continua not in "sn":
                system("cls" if "Win" in platform.system() else "clear")
                text.erro('Não entendi! Digite uma das opções válidas "s" ou "n"')
                continua = str(input('Deseja continuar?[S/N]: ').strip().lower())
            if continua == "n":
                system("cls" if "Win" in platform.system() else "clear")
                text.title("Finalizando o programa...")
                sleep(2)
                break
    except KeyboardInterrupt:
        print()
        text.marca('Programa finalizado pelo usuário. Até mais :D')



inicio()
