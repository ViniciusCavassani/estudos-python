dias_alugados = int(input('Por quantos dias o carro foi alugado? '))
quilometros = float(input('Quantos quilômetros foram percorridos? '))
custo_diarias = dias_alugados * 60
custo_quilometragem = quilometros * 0.15
total = custo_diarias + custo_quilometragem

print('Diárias: R${:.2f}.'.format(custo_diarias))
print('Quilometragem: R${:.2f}.'.format(custo_quilometragem))
print('Total: R${:.2f}.'.format(total))
