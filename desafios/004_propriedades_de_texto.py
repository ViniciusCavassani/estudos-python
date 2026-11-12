texto = input('Digite algo: ')

print('{} é numérico? {}'.format(texto, texto.isnumeric()))
print('{} é alfanumérico? {}'.format(texto, texto.isalnum()))
print('{} está em maiúsculas? {}'.format(texto, texto.isupper()))
print('{} é alfabético? {}'.format(texto, texto.isalpha()))
