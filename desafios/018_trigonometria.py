import math

angulo = float(input('Digite um ângulo em graus: '))
radianos = math.radians(angulo)
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print('Seno: {:.3f}'.format(seno))
print('Cosseno: {:.3f}'.format(cosseno))
print('Tangente: {:.3f}'.format(tangente))
