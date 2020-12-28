import json
from os import system
import sys

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
		for k, v in self.jogadores.items():
			print(f'Usuário: {k:^10} |  pontos: {v}'.center(80, ' '))




	def set_ponto(self, user):
		self.jogadores[user] += 30
		self.salvando()
		
