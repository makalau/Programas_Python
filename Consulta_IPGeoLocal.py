import requests
import socket
from os import system
import platform

def inicio():
    system("cls" if "Win" in platform.system() else "clear")
    print('-'*50)
    print('[ 1 ] Consultar IP    [ 2 ] Consulta HostName')
    print('-'*50)
    print()
    resp = str(input('Digite: ').strip())
    if resp == '1':
        ip = input('Digite o IP que deseja consultar: ').strip()
    else:
        hostname = str(input('Digite o Hostname que deseja consultar: ').strip())
        ip = socket.gethostbyname(hostname)
    
    url = f"https://api.ipgeolocation.io/ipgeo?apiKey=56c077eec32b46f6839ca726739fba28&ip={ip}&excludes=currency,time_zone"
    result = requests.get(url).json()
    for key, value in result.items():
        print('-'*66)
        print(f'{key:^15}| {value:>25}')
    print('-'*66)
    

inicio()