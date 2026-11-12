import random

nomes = input('Digite os nomes separados por espaços: ').split()
random.shuffle(nomes)

print('Ordem de apresentação: {}'.format(nomes))
