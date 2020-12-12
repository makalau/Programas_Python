import json
import os
import sys
import subprocess as sub


class Chatbot:
    def __init__(self, nome):
        try:
            with open('robot.json', 'r') as memoria:
                pass
        except FileNotFoundError:
            with open('robot.json', 'w') as memoria:
                memoria.write('[[], {"oi": "Olá, Qual seu nome?", "tchau": "tchau"}]')
        memoria = open('robot.json', 'r')
        self.nome = nome
        self.conhecidos, self.respostas = json.load(memoria)
        memoria.close()
        self.historico = []

    def escuta(self):
        frase = input('digite: ')
        if 'executar ' in frase:
            return frase
        frase = frase.lower()
        return frase

    def pensa(self, frase):
        if frase in self.respostas:
            return self.respostas[frase]

        if self.historico and self.historico[-1] == 'Olá, Qual seu nome?':
            nome = self.pega_nome(frase)
            resp = self.responde_nome(nome)
            self.historico.clear()
            return f'{resp}'

        elif 'aprender' in frase:
            key = input('Digite a palavra: ').strip()
            value = input('Digite o valor: ').strip()
            self.respostas[key] = value
            self.memoria()
            return 'Aprendido'

        if 'executar ' in frase:
            self.fala(frase)
            return 'executando...'

        else:
            return 'Não entendi'

    @staticmethod
    def pega_nome(nome):
        if 'meu nome ' in nome:
            nome = nome.split()[-1]
        nome = nome.title()
        return nome

    def responde_nome(self, nome):
        if nome in self.conhecidos:
            return f'Eai {nome}, bem vindo novamente'
        else:
            self.conhecidos.append(nome)
            self.memoria()
            return f'Prazer em conhecê-lo {nome}'

    def memoria(self):
        with open('robot.json', 'w') as memoria:
            json.dump([self.conhecidos, self.respostas], memoria)

    def fala(self, frase):
        if 'executar ' in frase:
            comando = frase.replace('executar ', '')
            system = sys.platform
            if 'win' in system:
                os.startfile(comando)
            elif 'linux' in system:
                try:
                    sub.Popen(comando)
                except FileNotFoundError:
                    comando = 'https://' + comando
                    sub.Popen(['xdg-open', comando])
        else:
            print(frase)
            self.historico.append(frase)



