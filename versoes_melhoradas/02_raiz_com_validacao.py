import math

numero = float(input('Digite um número: '))

if numero < 0:
    print('Não é possível calcular uma raiz quadrada real de um número negativo.')
else:
    print('A raiz quadrada de {} é {}.'.format(numero, math.sqrt(numero)))
