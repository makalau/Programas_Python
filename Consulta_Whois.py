import requests
from time import sleep
import platform
from os import system
from texto import text
import sys
import socket

text.marca("CONSULTA WHOIS")
while True:
    try:
        hostname = str(input('Digite o IP ou o hostname que deseja consultar: ').strip().lower())
        if hostname[0].isnumeric():
            lista_host = socket.gethostbyaddr(hostname)
            hostname = lista_host[0]
            
        consulta = requests.get(f'https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey=at_94Ps3mUz6JmnrVPSePLPRt8Ya9xHR&domainName={hostname}&outputFormat=json')
        result = consulta.json()
        dados = {
                    "Data de criação":result["WhoisRecord"]["createdDate"],
                    "Atualizado em":result["WhoisRecord"]["updatedDate"],
                    "Organização registrada":result["WhoisRecord"]["registrant"]["organization"],
                    "Estado":result["WhoisRecord"]["registrant"]["state"],
                    "País":result["WhoisRecord"]["registrant"]["country"],
                    "código":result["WhoisRecord"]["registrant"]["countryCode"],
                    "Nome do domínio":result["WhoisRecord"]["domainName"],
                    "HostName dos servidores": result["WhoisRecord"]["nameServers"]["hostNames"],
                     "IP":result["WhoisRecord"]["nameServers"]["ips"],
                     "Parse Code":result["WhoisRecord"]["parseCode"],
                     "Registrar Nome":result["WhoisRecord"]["registrarName"],
                     "Registro ID":result["WhoisRecord"]["registrarIANAID"],
                     "Email contato":result["WhoisRecord"]["contactEmail"],
                     "domainNameExt":result["WhoisRecord"]["domainNameExt"],
                     "Registrar Nome":result["WhoisRecord"]["estimatedDomainAge"]
                    }
                    
        system("cls" if platform.system() == "Windows" else "clear")
        print('Processando....')
        sleep(2)
        print()
        print('-'*66)
        print('\033[34m           Tables              |           Values          \033[m')
        for key, value in dados.items():
            if isinstance(value, list) or isinstance(value, tuple):
                cont = 1
                for indice in value:
                    print('-'*66)
                    print(f'{cont}º - {key:^24}  |  {indice:^30}')
                    cont += 1
            else:
                print('-'*66)
                print(f'{key:^30} | {value:^30}')
            
        print('-'*66)
        continua = str(input('Deseja realizar uma nova consulta?[s/n]').strip().lower())
        while not continua or continua not in "sn":
            text.title("Não entendi! Digite uma das opções válidas [ s ]  ou [ n ];")
            continua = str(input('Deseja realizar uma nova consulta?[s/n]').strip().lower())
        if continua == "n":
            system("cls" if platform.system() == "Windows" else "clear")
            print("Programa finalizado com sucesso!")
            break
        system("cls" if platform.system() == "Windows" else "clear")
    except KeyboardInterrupt:
        system("cls" if platform.system() == "Windows" else "clear")
        text.title("Programa finalizado pelo usuário...")
        sys.exit()


