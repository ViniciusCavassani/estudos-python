reais = float(input('Quantos reais você tem? R$ '))
taxa = float(input('Qual taxa em reais por dólar deseja usar? '))

if taxa <= 0:
    print('A taxa precisa ser maior que zero.')
else:
    dolares = reais / taxa
    print('Com R${:.2f}, usando a taxa informada, o resultado é US${:.2f}.'.format(
        reais, dolares
    ))
