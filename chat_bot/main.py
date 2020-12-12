from interface import *
from datetime import datetime
def main():
	print(f'Data atual:  {datetime.now()}')
	print('-=-=-=-=-= BEM VINDO AO CHAT BOT -=--=-=-=')
	print('Digite algo para iniciar o diálogo')
	robot = Chatbot('Naomy')
	while True:
		ouvir = robot.escuta()
		resp = robot.pensa(ouvir)
		robot.fala(resp)
		if resp == 'tchau':
		    break
	print('Encerrando o programa....')

try:
	main()
except KeyboardInterrupt:
	print("\nFinalizando o Programa.. Volte sempre!")
