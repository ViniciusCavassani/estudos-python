import random

nomes = input('Digite os nomes separados por espaços: ').split()
nome_sorteado = random.choice(nomes)

print('O nome sorteado foi {}.'.format(nome_sorteado))
