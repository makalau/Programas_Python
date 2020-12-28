from time import sleep

def titulo(texto, texto2=None):
	print()
	tamanho = len(texto)
	print('\033[1;33m', '-' * 80,'\033[1;m')
	print(texto.center(80, ' '))
	if texto2:
		print('\033[1;m', texto2.center(80, ' '))
	print('\033[1;33m','-' * 80)
	print()
	print()

def linha():
	print('-' * 80)

def centro(texto):
        print(texto.center(90, ' '))


def loading(texto, sec=0.5):
	print(texto, end='')
	for c in range(4):
		print('.', end='', flush=True)
		sleep(sec)
	print()
