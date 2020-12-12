# python 3.6
""" Programa que usa fórmulas e parâmetros reais para calcular o IMC, e identificar a classificação de acordo com os
dados expostos pelo Ministério da Saúde no que se refere a qualidade do IMC. Vamos lá"""
from time import sleep
# =-=-==-= Cores =-=-=-=-=-=
amarelo = '\033[1;32m'
vermelho = '\033[1;31m'
branco_n = '\033[;1m'


def estrutura_geral():
    abertura()
    calculo()


def abertura():
    print(f'{vermelho}-='*28, f'{amarelo}')
    print(f' Bem vindo a calculadora do IMC. '.center(50, '>'))
    print(f'{branco_n}-Responda o questionário para saber se está dentro\n dos limites considerados '
          'saudáveis para o seu IMC.')
    print(f'{vermelho}-='*28, f'{branco_n}')


def calculo():
    try:
        peso = float(input('Qual seu peso?: '))
        altura = float(input('Qual sua altura?: '))
        imc = peso/(altura**2)
    except ValueError:
        print('Valor inválido! Tente novamente.')
    else:
        print('Calculando.....')
        sleep(0.5)
        print(f'O seu IMC é de: {imc:.2f}')
        if 18.5 <= imc < 25:
            print('PARABÉNS! Seu IMC está saudável. [Ideal]')

        elif 25 < imc <= 30:
            print('CUIDADO, está um pouco acima do IMC ideal [18.5-25] [Sobrepeso]')

        elif 30 < imc:
            print('ATENÇÃO! seu quadro já é caracterizado [obesidade], está muito acima do recomendado.')

        elif 18.5 > imc:
            print('ATENÇÃO, está abaixo do IMC recomendado.')


estrutura_geral()

