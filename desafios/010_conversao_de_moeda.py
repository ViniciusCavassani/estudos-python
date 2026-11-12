# Taxa fixa usada somente para este exercício didático.
taxa_didatica = 5.50
reais = float(input('Quantos reais você tem? R$ '))
dolares = reais / taxa_didatica

print('Com R${:.2f}, o resultado é US${:.2f} usando a taxa didática de R${:.2f}.'.format(
    reais, dolares, taxa_didatica
))
