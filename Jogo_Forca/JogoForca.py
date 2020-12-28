# python 3.6
'''Jogo da Forca, esse jogo necessita de um documento extensão .txt na mesma pasta do programa, para a obtenção 
das palavras-chave que serão utilizada no jogo.''' 

from time import sleep
from random import randint
import sys
import re
import os
from players import jogadores
from players import texto

class Jogo(jogadores.Jogador):
	def analise(self):
		if len(sys.argv) < 2:
			print("-" * 72)
			# Se não for passado nenhum argumento, a mensagem abaixo será mostrada e em seguida finalizar o programa.
			print("\033[1;33mPasse um arquivo.txt como argumento:\n - Contendo palavras que gostaria que "
		   		  "fosse usadas no jogo.")
			print("\033[1;m","-" * 72)
			sys.exit()

		else:
			# Análise de entrada do argumento. programa aceita apenas arquivos com extensão (txt) de texto.
			self.argv = sys.argv[1]
			padrao = re.compile(r"\w+\.txt")
			procurar = padrao.search(self.argv)

			if procurar:
				try:
					with open(self.argv, "r") as arquivo:
						pass

				except FileNotFoundError:
					print("-" * 72)
					print("\033[1;33mArquivo não encontrado. Coloque-o na pasta do programa e verifique a "
		                  "ortografia.\033[1;m")
					print("-" * 72)

				else:
					self.nome = list()
					self.abertura()
			else:
				print("-"*72)
				print("\033[1;33mArquivo de texto não identificado. insira: nome_arquivo.txt\033[m")
				print("-"*72)

	def abertura(self):
		os.system("cls" if 'win' in sys.platform else "clear")
		print('Carregando', end='')
		for c in range(0, 4):
			print('.', end='', flush=True)
			sleep(0.5)
		print('\033[1;36m')
		print(' ' * 17, '+------------------------+')
		print(' ' * 17, '|      Jogo Da Forca     |')
		print(' ' * 17, '+------------------------+\033[m')
		print(' ' * 24, '\033[1;mMenu Princial\033[1;36m')
		print('+-----------------+------------------+-------------------------+')
		print('| [i]-Instruções  | Enter - Continue | S - Sair | R - Ranking  |')
		print('+-----------------+------------------+-------------------------+\033[m')

		opcoes = str(input('\033[1;mResponda: ').strip().lower())

		if opcoes == 'i':
			print("-" * 72)
			print('Intruções: Se trata de um jogo de adivinhação.\nVocê terá que adivinhar qual a Palavra-Chave.'
                  'Poderá usar desde pequenos chutes de letras-\n-que acredita compor a palavra,'
                  ' até chutes de palavras completas.\n'
                  '\033[1;33m\nLembrando que:\033[m \n   * Se chutar uma palavra completa e errar é GAME OVER.\n'
                  '   * Se chutar 4 letras que a palavra não contém é GAME OVER. '
                  '\n   * Caso queira arriscar um chute ao invés de digitar uma letra digite a palavra: Chute.')
			print('Digite alguma letra para voltar ao Menu Principal')
			resp = input(': ')
			self.abertura()

		elif opcoes == 'r':
			self.consulta()
			print('Digite alguma letra para voltar ao Menu Principal')
			resp = input(': ')
			self.abertura()
		elif opcoes == "s":
			encerramento()

		else:
			os.system("cls" if 'win' in sys.platform else "clear")
			print('Qual modo quer jogar?')
			print('[ 1 ] - SinglePlayer   [ 2 ] MultiPlayer')
			resp = 0
			while not resp or resp not in range(1, 3):
				try:
					resp = int(input('Responda: '))
					if resp not in range(1, 3):
						print('tecle [ 1 ] ou [ 2 ], conforme as opções desejadas')
					
				except ValueError:
					print('tecle [ 1 ] ou [ 2 ], conforme as opções desejadas')

			os.system("cls" if 'win' in sys.platform else "clear")
			if not self.nome:
				self.nome.append(str(input('Nome do 1º jogador: ').strip().capitalize()))
				
			if resp == 2:
				self.nome.append(str(input('Nome do 2º jogador: ').strip().capitalize()))
			texto.loading('carregando')
			os.system("cls" if 'win' in sys.platform else "clear")
			for pessoa in self.nome:			
				self.registro(pessoa)
			self.pegar_palavra()


	def pegar_palavra(self):
		palavras = list()
		# a lista chamada palavra, irá clonar todas palavras do arquivo de texto e em seguida fechá-lo.
		with open(self.argv, "r") as arquivo:
			for linha in arquivo:
				palavras.append(linha)

		misto = randint(0, len(palavras) - 1)
		palavra_escolhida = palavras[misto].lower().strip()
		self.analise_jogo(palavra_escolhida)


	def analise_jogo(self, palavra_chave):
		letras_chute = []
		variavel = ['_ '] * len(palavra_chave)
		erro = 0
		cont = 0
		resposta = ''
		self.venceu = ''
		if not self.venceu:
			nome = self.nome[0]
		else:
			nome = self.venceu

		while erro < 5 or resposta != 'chute':
			print(f'\033[1;33mDica:\033[1;m A palavra possui {len(palavra_chave)} letras')
			print()
			cont += 1
			if erro == 5:
				self.enforcado(palavra_chave)
				break
                

			if str("".join(variavel)) == palavra_chave:
				print(f"\033[1;33mPARABÉNS! VOCÊ VENCEU!!\n\033[mPalavara chave era: {palavra_chave.title()}")
				vencedor(nome)
				break

			elif erro == 4:
				print()
				print(f"\033[1;31mATENÇÃO: \033[1;mÚLTIMA tentativa! \033[1;mtotal de erros: \033[1;31m{erro}\033[1;m")
				print()

			else:
				texto.linha()
				print(f'\033[33m{cont}ª Tentativa!  \033[mTotal de erros: \033[1;31m{erro}\033[1;m') 
			print('\n'*2)
			print('\033[1;36mPalavra_chave:\033[1;m  ', end=' ')
			for elemento in variavel:
				print(elemento, end=' ')
			while True:
				print('\n'*1)
				texto.linha()
				resposta = str(input(f'\033[1;33m[ {nome} ] \033[1;m- Digite uma letra: ').lower().strip())
				if len(resposta) > 1 and resposta != "chute":
					print("\n\033[31mEntrada inválida!\033[m Digite apenas uma letra.")				        
				else:
					break
			letras_chute.append(resposta)

			# Limpeza de tela multiplataforma, se for windows "cls" se for Linux(posix) "clear"
			os.system("cls" if 'win' in sys.platform else "clear")

			print("\033[33mletras chutadas até agora: ", end=" ")
			for letras in letras_chute:
				print(f"{letras}", end=" ")

			print("\033[37m\npressione Ctrl+c a qualquer momento caso queira sair do programa.")
			print('-' * 80, '\033[m')
			sleep(0.2)
			print()

			if resposta in palavra_chave:
				texto.loading('Processando')
				print('Para voltar ao Menu Principal, responda: [ 0 ]')
				print(
                    f'\033[1;mExistem \033[1;33m{palavra_chave.count(resposta)}\033[1;m ocorrências da palavra '
                    f'"\033[1;33m{resposta}\033[1;m"')
				print()
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
					acertou = False
					if erro <= 4:
						print(f'\033[1;mNão tem essa letra na palavra.', end='')
         
						if erro < 4:
							print(f'\033[1;31m CUIDADO\033[1;m: você errou: \033[1;31m{erro}\033[1;m', end=' ')
							if erro == 1:
								print("vez.")
							else:
								print("vezes.")
						sleep(1)
						if len(self.nome) > 1:
							nome = self.nome[1] if nome == self.nome[0] else self.nome[0]
						print()

				if resposta == 'chute':
					self.chute(palavra_chave, nome)
					break


	def chute(self,chave, nome):
		chute_certo = input('\033[1;mDigite a palavra que acredita ser: ').strip().lower()
		if chute_certo == chave:
			print()
			print(f'\033[1;33mPARABÉNS {nome}!! \033[mVocê acertou, a palavra chave é: \033[1;33m{chave}\033[m')
			self.vencedor(nome)

		else:
			print()
			if len(self.nome) > 1:
				print(f"\033[1;31m\nGAME OVER! VOCÊS FORAM ENFORCADOS!\n\033[mA palavra certa era:\033[1;33m {chave}\033[m")
			else:
				print(f"\033[1;31m\nGAME OVER! VOCÊ FOI ENFORCADO!\n\033[mA palavra certa era:\033[1;33m {chave}\033[m")
			self.enforcado(chave)


	def enforcado(self, palavra):
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
		self.continua()


	def vencedor(self, nome):
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
		self.set_ponto(nome)
		self.venceu = nome
		self.continua()


	def continua(self):
		pergunta = input("\033[mdeseja jogar novamente?[s/n]: ").strip().lower()

		if pergunta == "s":
			os.system("cls" if "win" in sys.platform else "clear") 
			self.pegar_palavra()

		else:
			self.encerramento()

	def encerramento(self):
		os.system("cls" if 'win' in sys.platform else "clear")
		texto.loading("encerrando o programa")
		texto.titulo("Programa finalizado com Sucesso!", "Volte sempre")
        
try:
	jogo =  Jogo()
	jogo.analise()
	
except KeyboardInterrupt:
	os.system("cls" if 'win' in sys.platform else "clear")
	texto.loading("encerrando o programa")
	texto.titulo("Programa finalizado com Sucesso!", "Volte sempre")


