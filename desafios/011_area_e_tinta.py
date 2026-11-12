largura = float(input('Qual é a largura da parede em metros? '))
altura = float(input('Qual é a altura da parede em metros? '))
area = largura * altura
litros_de_tinta = area / 2

print('A área da parede é {:.2f} m².'.format(area))
print('Pela regra de 1 litro para cada 2 m², serão necessários {:.2f} L.'.format(
    litros_de_tinta
))
