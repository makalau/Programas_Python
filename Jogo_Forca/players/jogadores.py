import json
from os import system
import sys
from operator import itemgetter
from players import texto

class Jogador:
	def __init__(self):
		try:
			with open('ranking.json', 'r') as registro:
				pass
		except FileNotFoundError:
			print('nao tem')
			with open('ranking.json', 'w') as registro:
				registro.write('{}')
		registro = open('ranking.json', 'r')
		self.jogadores = json.load(registro)
		registro.close()	

	def registro(self, nome):
		if nome in self.jogadores:
			pass

		else:
			pontos = 0
			self.jogadores[nome] = pontos
			self.salvando()
			system("cls" if sys.platform in 'win' else "clear")
			print('Novo usuário cadastrado com êxito!')

	def salvando(self):
		with open('ranking.json', 'w') as cadastro:
			json.dump(self.jogadores, cadastro)

	def consulta(self):
		texto.titulo('Ranking dos Jogadores!')
		print(f'jogadores cadastrados: {len(self.jogadores)}')
		print('\n'*2)
		texto.linha()
		order = list()
		order = sorted(self.jogadores.items(), key=itemgetter(1), reverse=True)
		print(f'{"POSIÇÃO":<17}{"NOME":<13}{"PONTUAÇÃO	":>12}'.center(79, ' '))
		texto.linha()		
		for p, v in enumerate(order):
			print(f'{p+1}ºlugar - {v[0]:^20} - {v[1]} pontos'.center(80, ' '))
			texto.linha()
		print()
	


	def set_ponto(self, user):
		self.jogadores[user] += 30
		self.salvando()
		
