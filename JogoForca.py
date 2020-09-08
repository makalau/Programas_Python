from time import sleep
from random import randint
import sys
import re
import os

try:
    def jogo():
        if len(sys.argv) < 2:
            print()
            print("passe um arquivo.txt como argumento\ncontendo palavras que gostaria que fosse usadas para o jogo.")
            print()
            sys.exit()

        else:
            argv = sys.argv[1]
            padrao = re.compile(r"\w+\.txt")
            procurar = padrao.search(argv)

            if procurar == None:
                print("Digite um argumento válido para arquivo de texto com extensão .txt")

            else:
                abertura(argv)


    def abertura(argumento):

        print('' * 5, '\033[1;mIniciando o Jogo', end='')
        for c in range(0, 4):
            print('.', end='')
        print('\033[1;36m')
        print(' ' * 9, '+------------------------+')
        print(' ' * 9, '|      Jogo Da Forca     |')
        print(' ' * 9, '+------------------------+\033[m')
        print(' ' * 16, '\033[1;mMenu Princial\033[1;36m')
        print('+-----------------+------------------+----------+')
        print('| [i]-Instruções  | Enter - Continue | S - Sair |')
        print('+-----------------+------------------+----------+\033[m')

        opcoes = str(input('\033[1;mResponda: ').strip().lower())

        if opcoes == 'i':
            print('Intruções: Se trata de um jogo de adivinhação, você terá que adivinhar qual a Palavra-Chave.'
                  '\n-Podera usar desde pequenos chutes de letras que acredita compor a palavra,'
                  ' até chutes de palavras completas.\n'
                  '-Lembrando que: Se chutar uma palavra completa e errar é GAME OVER.\n'
                  '-Se chutar 4 letras que a palavra não contém é GAME OVER. '
                  '\n-Caso queira arriscar um chute ao invés de digitar uma letra digite a palavra: Chute.')

            print()
            print('Digite alguma letra para saber se ela está contida na palavra-chave:')
            pegar_palavra(argumento)

        elif opcoes == "s":
            print("finalizando o programa...")

        else:
            pegar_palavra(argumento)


    def pegar_palavra(argumento):
        arquivo = open(argumento, "r")
        palavras = list()
        for linha in arquivo:
            palavras.append(linha)
        arquivo.close()
        misto = randint(0, len(palavras)-1)
        palavra_escolhida = palavras[misto].lower().strip()
        analise_jogo(palavra_escolhida)


    def analise_jogo(palavra_chave):
        variavel = ['_ ']*len(palavra_chave)
        erro = 0
        cont = 0
        resposta = ''
        while erro <= 4 or resposta != 'chute':
            cont += 1
            if erro == 4:
                enforcado(palavra_chave)
                break
            print()
            print(f'\033[1;31m{cont}ª Tentativa!  Total de erros: {erro}\033[m')

            for elemento in variavel:
                print(elemento, end=' ')
            print()
            print()
            resposta = str(input('\033[1;mDigite uma letra: ').lower().strip())
            os.system("clear")
            print("\033[37mpressione Ctrl+c a qualquer momento caso queira sair do programa.")
            print('-' * 80, '\033[m')
            sleep(0.2)
            print()
            if resposta in palavra_chave:
                print('\033[1;36mprocessando...\033[1;m')
                sleep(2)
                print()
                print(f'\033[1;mExistem \033[1;32m{palavra_chave.count(resposta)}\033[1;m ocorrências da palavra "\033[1;32m{resposta}\033[1;m"')
                sleep(1)
                for posicao, elemento in enumerate(palavra_chave):
                    if elemento == resposta:
                        variavel[posicao] = resposta
            else:
                if resposta != 'chute':
                    print('\033[1;36mprocessando...\033[m')
                    sleep(2)
                    erro += 1
                    print()
                    print(f'\033[1;mNão tem essa letra na palavra.', end='')
                    if erro < 6:
                        print(f'\033[1;31mCUIDADO\033[1;m: você errou \033[1;31m{erro}\033[1;m vezes.')
                        sleep(1)
                        print()

                if resposta == 'chute':
                    chute(palavra_chave)
                    break


    def chute(chave):
        chute_certo = input('\033[1;mDigite a palavra que acredita ser: ').strip().lower()
        if chute_certo == chave:
            print()
            print(f'\033[1;32mPARABÉNS!! Você acertou a palavra chave é: \033[1;m{chave}')
            vencedor()

        else:
            print()
            enforcado(chave)


    def enforcado(palavra):
        print("\033[1;31m\nGAME OVER! VOCÊ FOI ENFORCADO!\n\033[mA palavra certa era:\033[1;33m", palavra)
        print('\033[1;31m')
        print("    _________________")
        print("   /                 \ ")
        print("  /                   \ ")
        print(" /                     \ ")
        print(" |    xxxx     xxxx    | ")
        print(" |    xxxx     xxxx    |")
        print(" |    xxx       xxx    |")
        print(" \__       xxx       __/")
        print("    |\     xxx     /|")
        print("    | |           | |")
        print("    | I I I I I I I |")
        print("    |  I I I I I I  |")
        print("    \_             _/")
        print()

        pergunta = input("\033[mdeseja jogar novamente?[s/n]: ").strip().lower()
        if pergunta == "s":
            abertura(sys.argv[1])
        else:
            sys.exit()

    def vencedor():
        print("\033[1;33m")
        print("")
        print("             _______________  ")
        print("           '._=_==_==_==_==_.' ")
        print("           .-\ \:          /-.")
        print("          | (|:.          |) |")
        print("           '-|:.          |-' ")
        print("              \ \::.      /  ")
        print("                '::.  .'     ")
        print("                   ) (       ")
        print("                _.'   '._    ")
        print("               '---------'   \033[m")
        print()

        pergunta = input("deseja jogar novamente?[s/n]: ").strip().lower()
        if pergunta == "s":
            abertura(sys.argv[1])
        else:
            sys.exit()

    jogo()

except KeyboardInterrupt:
    print()
    print('-' * 80)
    print(" " * 16, "\033[33mPrograma finalizado com Sucesso!")
    print(" " * 27, "Volte Sempre!\033[m")
    print('-' * 80)
