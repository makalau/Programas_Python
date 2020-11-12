'''Python 3.6
Esse programa usa um método de cálculo baseado na ordem alfabética do hebraico e regras da numerologia cabalística para
identificar o número correspondente ao nome completo de uma pessoa e as energias que emanam sobre ela. Onde cada letra do
alfabeto se identifica por um número específico (conforme a tabela).
fonte: Tabela base extraída do site: www.astrocentro.com.br/blog/numerologia/numerologia-cabalistica.'''

lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'x', 'y', 'z']

nomeDict = dict()
cont = 0
for c in lista:
    if cont < 10:
        cont += 1
        nomeDict[c] = cont

    if c == 'i':
        cont -= 1
        nomeDict['j'] = cont

    if 100 >= cont >= 10:
        nomeDict[c] = cont
        cont += 1 * 10

    if c in 'uvw':
        nomeDict[c] = 200
    if c in 'xyz':
        nomeDict['x'] = 300
        nomeDict['y'] = 9
        nomeDict['z'] = 400
# Nome completo de preferência.
nome = str(input('Digite seu nome completo: ').strip().lower()).split()
junta = ''.join(nome)
soma = total = resto = 0
for letra in junta:
    soma += nomeDict[letra]

for x in str(soma):
    total += int(x)

# Se o total for 22 ou 11 pela regra, não podemos somá-los entre sí, pois são números mestres.
if len(str(total)) >= 2 and total not in (11, 22):
    for c in str(total):
        resto += int(c)
print(f'O número cabalístico do seu nome é:', end=' ')
print(resto if resto else total)

