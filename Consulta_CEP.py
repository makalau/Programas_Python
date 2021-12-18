import requests
from os import system
from time import sleep
import requests
import platform

def menu():
    system("cls" if "Win" in platform.system() else "clear")
    print()
    print('+'+'-'*60+'+')
    print('|', ' '*59+'|')
    print('|', "######################".center(59, ' ')+'|')
    print('|', "#### Consulta CEP ##".center(59, ' ')+'|')
    print('|', "######################".center(59, ' ')+'|')
    print('|', ' '*59+'|')
    print('+'+'-'*60+'+')
    print()
    query()

def query():
    cep = input('Digite seu CEP: ').strip()
    while len(cep) != 8:
        print('-'*80)
        print('Valor de CEP inválido! O CEP deve conter 8 dígitos, confira e tente novamente')
        print('-'*80)
        cep = input('Digite seu CEP: ').strip()
    print('Processando....')
    request = requests.get(f"http://viacep.com.br/ws/{cep}/json/")
    sleep(2)
    system("cls" if "Win" in platform.system() else "clear")
    result = request.json()
    if 'erro' not in result:    
        for key,values in result.items():
            print('+'+'-'*42+'+')
            print(f"| {key:^11} | {values:>25}  |")
        print('+'+'-'*42+'+')

    else:
        print('CEP inválido! ')

    continua = str(input('Deseja fazer uma nova consulta?[S/N]: ').strip().lower())
    while continua not in "sn":
        print('-'*20)
        print('Opção inválida!')
        print('-'*20)
        continua = str(input('Deseja fazer uma nova consulta?[S/N]: ').strip().lower())
    if continua == 'n':
        system("cls" if "Win" in platform.system() else "clear")
        print('Finalizando o programa. Por favor aguarde....')
        sleep(3)
    else:
        menu()

menu()