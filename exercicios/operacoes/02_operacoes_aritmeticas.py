numero1 = int(input('Digite um valor: '))
numero2 = int(input('Digite outro valor: '))

soma = numero1 + numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
divisao_inteira = numero1 // numero2
potencia = numero1 ** numero2

print('A soma é {}, a multiplicação é {} e a divisão é {:.4f}.'.format(
    soma, multiplicacao, divisao
))
print('A divisão inteira é {} e a potência é {}.'.format(
    divisao_inteira, potencia
))
