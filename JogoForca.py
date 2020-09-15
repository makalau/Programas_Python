from time import sleep
from random import randint
import sys
import re
import os


try:
    def jogo():
        if len(sys.argv) < 2:
            print("-" * 80)
            # Se não for passado nenhum argumento, a mensagem abaixo será mostrada e em seguida finalizar o programa.
            print("\033[1;33mPasse um arquivo.txt como argumento:\n - Contendo palavras que gostaria que "
                  "fosse usadas no jogo.")
            print("\033[1;m","-" * 79)
            sys.exit()

        else:
            # Análise de entrada do argumento. programa aceita apenas arquivos com extensão (txt) de texto.
            argv = sys.argv[1]
            padrao = re.compile(r"\w+\.txt")
            procurar = padrao.search(argv)

            if procurar == None:
                # se o argumento passado não for um arquivo de texto, programa irá rejeitar e encerrar.
                print("Digite um argumento válido para arquivo de texto com extensão .txt")

            else:
                try:
                    arquivo =  open(argv, "r")

                except FileNotFoundError:
                    print("-" * 80)
                    print("\033[1;33mArquivo não encontrado. Coloque-o na pasta do programa e verifique a "
                          "ortografia.\033[1;m")
                    print("-" * 80)
                else:
                    arquivo.close()
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
            print("-" * 89)
            print('Intruções: Se trata de um jogo de adivinhação.\nVocê terá que adivinhar qual a Palavra-Chave.'
                  'Poderá usar desde pequenos chutes de letras-\n-que acredita compor a palavra,'
                  ' até chutes de palavras completas.\n'
                  '\033[1;33m\nLembrando que:\033[m \n   * Se chutar uma palavra completa e errar é GAME OVER.\n'
                  '   * Se chutar 4 letras que a palavra não contém é GAME OVER. '
                  '\n   * Caso queira arriscar um chute ao invés de digitar uma letra digite a palavra: Chute.')

            print("-" * 89)
            print('Digite alguma letra para saber se ela está contida na palavra-chave:')
            print()
            pegar_palavra(argumento)

        elif opcoes == "s":
            encerramento()

        else:
            pegar_palavra(argumento)


    def pegar_palavra(argumento):
        arquivo = open(argumento, "r")
        palavras = list()
        # a lista chamada palavra, irá clonar todas palavras do arquivo de texto e em seguida fechá-lo.
        for linha in arquivo:
            palavras.append(linha)
        arquivo.close()

        misto = randint(0, len(palavras) - 1)
        palavra_escolhida = palavras[misto].lower().strip()
        analise_jogo(palavra_escolhida)


    def analise_jogo(palavra_chave):
        letras_chute = []
        variavel = ['_ '] * len(palavra_chave)
        erro = 0
        cont = 0
        resposta = ''
        while erro < 5 or resposta != 'chute':
            cont += 1
            if erro == 5:
                enforcado(palavra_chave)
                break

            print()
            if erro == 4:
                print()
                print(f"\033[1;31mATENÇÃO: \033[1;mÚLTIMA tentativa! \033[1;mtotal de erros: \033[1;31m{erro}\033[1;m")
                print()
            
            else:
                print(f'\033[1;33m{cont}ª Tentativa!  \033[1;mTotal de erros: \033[1;31m{erro}\033[1;m')

            for elemento in variavel:
                print(elemento, end=' ')
            print()
            print()
            valida = 0

            while valida == 0:
                resposta = str(input('\033[1;mDigite uma letra: ').lower().strip())

                if len(resposta) > 1 and resposta != "chute":
                    print("\n\033[31mEntrada inválida!\033[m Digite apenas uma letra.")
                    valida = 0
                else:
                    valida = 1

            letras_chute.append(resposta)

            # Limpeza de tela multiplataforma, se for windows "cls" se for Linux(posix) "clear"
            os.system("cls" if os.name == "nt" else "clear")

            print("\033[33mletras chutadas até agora: ", end=" ")
            for letras in letras_chute:
                print(f"{letras}", end=" ")

            print("\033[37m\npressione Ctrl+c a qualquer momento caso queira sair do programa.")
            print('-' * 80, '\033[m')
            sleep(0.2)
            print()

            if resposta in palavra_chave:
                print('\033[1;36mprocessando...\033[1;m')
                sleep(2)
                print()
                print(
                    f'\033[1;mExistem \033[1;33m{palavra_chave.count(resposta)}\033[1;m ocorrências da palavra '
                    f'"\033[1;33m{resposta}\033[1;m"')
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
                    if erro <= 4:
                        print(f'\033[1;mNão tem essa letra na palavra.', end='')
                    
                    if erro < 4:
                        print(f'\033[1;31m CUIDADO\033[1;m: você errou: \033[1;31m{erro}\033[1;m', end=' ')
                        if erro == 1:
                            print("vez.")
                        else:
                            print("vezes.")
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
        continua()


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
        continua()


    def continua():
        pergunta = input("\033[mdeseja jogar novamente?[s/n]: ").strip().lower()

        if pergunta == "s":
            abertura(sys.argv[1])

        else:
            encerramento()


    def encerramento():
        os.system("cls" if os.name == "nt" else "clear")
        print("encerrando o programa....")
        sleep(2)
        print()
        print('-' * 80)
        print(" " * 16, "\033[33mPrograma finalizado com Sucesso!")
        print(" " * 27, "Volte Sempre!\033[m")
        print('-' * 80)
        print()


    jogo()
except KeyboardInterrupt:
    os.system("cls" if os.name == "nt" else "clear")
    print("encerrando o programa....")
    sleep(2)
    print()
    print('-' * 80)
    print(" " * 16, "\033[33mPrograma finalizado com Sucesso!")
    print(" " * 27, "Volte Sempre!\033[m")
    print('-' * 80)
    print()

