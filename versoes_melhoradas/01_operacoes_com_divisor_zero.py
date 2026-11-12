numero1 = int(input('Digite um valor: '))
numero2 = int(input('Digite outro valor: '))

print('Soma: {}'.format(numero1 + numero2))
print('Multiplicação: {}'.format(numero1 * numero2))

if numero2 == 0:
    print('As divisões não foram calculadas porque o segundo valor é zero.')
else:
    print('Divisão: {:.4f}'.format(numero1 / numero2))
    print('Divisão inteira: {}'.format(numero1 // numero2))

print('Potência: {}'.format(numero1 ** numero2))
