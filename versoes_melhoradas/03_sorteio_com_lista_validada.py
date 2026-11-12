import random

entrada = input('Digite os nomes separados por vírgulas: ')
omes = []

for nome in entrada.split(','):
    nome = nome.strip()
    if nome:
        nomes.append(nome)

if nomes:
    print('O nome sorteado foi {}.'.format(random.choice(nomes)))
else:
    print('Nenhum nome foi informado.')
