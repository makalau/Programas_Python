#! python3.6
# Programa para a identificação e obtenção de dados específicos em ambiente web ou documentos de textos.
# O programa conta com 2 funcionalidades via pyperclip(texto copiado pelo sistema) ou manipulando arquivos.txt

import re
import pyperclip
import sys
from time import sleep

print('\033[33m')
print("BEM VINDO AO INDENTICADOR DE PADRÕES PYTHON!".center(80, '_'))


def inicio():
    print()
    if len(sys.argv) < 2:  # Pré-análise para identificar se foi passado um argumento..
        # Se o argumento for omitido programa fará varredura nos dados copiados pelo sistema via (pyperclip).
        print("\033[mAguarde enquanto o programa escaneia os dados copiados para pyperclip...\033[37m")
        sleep(2)
        print()
        # variavel lines armazena dados copiados. Method split usa as quebra de linha \n e as transforma em índices.
        # Tornando mais fácil a manipulação.
        lines = pyperclip.paste().split('\n')

        copia = list()
        # laço for para vasculhar cada elemento e adicionar em uma nova lista de forma que não ocorra "dados repetidos"
        for elemento in lines:
            if elemento not in copia:
                copia.append(elemento)

        # lista repassada em argumento com formato string, pois o método de compilação de padrões não é compatível ao-
        #-type: list.
        telefone_email(str(copia))

    else:  # Identificar o tipo de argumento passado.
        argumento = sys.argv[1]
        padrao_argumento = re.compile(r"\w+.txt")
        objeto = padrao_argumento.search(argumento)

        # Critérios para a entrada de argumentos
        if objeto:
            try:
                arquivo = open(argumento, "r")

            except FileNotFoundError:
                print('\033[m-' * 72)
                print("\033[1;33mArquivo não encontrado. \033[mVerifique se o arquivo está na pasta do programa.")
                print('-' * 72)
                print()

            else:
                arquivo.close()
            # OPÇÃO 1 - Varrer arquivo de texto e chamar a função de manipulação de documentos.txt para encontrar padrões.
                print(f"\033[mAnalizando o documento {objeto.group()} (processando....)")
                sleep(2)
                print()
                documento(argumento)
        
        else:
            print(" " * 4, "\033[1;31mATENÇÃO:\033[1;36m")
            print(' '*11, '+' + '-'*44 + '+')
            print(" "*11, "|\033[m-insira um documento com extensão: \033[1;31m.txt\033[1;36m", " "*3, "|")
            print(" "*11, "|\033[mou omite o argumento para entrada pyperclip.\033[1;36m|")
            print(" "*11, "+" + "-"*44 + "+\033[m")
            print()



def documento(arquivo):
    dados = []
    doc = open(arquivo, "r")
    leitura = doc.readlines()

    for linha in leitura:
        if linha not in dados:
            dados.append(linha)
    doc.close()

    dados = ' '.join(dados)
    telefone_email(dados)


def telefone_email(texto):
    # expressões regulares. padrão telefone e email.

    telefone = re.compile(r"""((\d{2}|\(\d{2}\))
                            (\s|-|\.)?
                            \d{4,5}
                            (\s|-|\.)?
                            \d{4})""", re.VERBOSE)

    email = re.compile(r"(\w+@\w+\.com(\.br)?)")

    procurar_email = email.findall(texto)
    procurar = telefone.findall(texto)

    if len(procurar) < 1:
        print("".ljust(2), "\033[31mNão foram encontrados padrões correspondentes à um telefone.\033[m")

    else:
        print('-'*20 + "padrões de telefone" + '-'*20)
        print()
        for pos in range(len(procurar)):
            print(f"Telefone: \033[33m{procurar[pos][0]}\033[m")

    if len(procurar_email) < 1:
        print(''.ljust(2), "\033[31mNão foram encontrados padrões correspondentes à um E-mail.\033[m")
        print()
    else:
        print('-'*20 + "padrões de email" + '-'*20)
        print()
        for pos in range(len(procurar_email)):
            print(f"Email: \033[33m{procurar_email[pos][0]}\033[m")


inicio()
