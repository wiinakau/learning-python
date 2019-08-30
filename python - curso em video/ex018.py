from math import sin, cos, tan, radians

angulo = float(input('Digite o valor do angulo: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O seno é: {:.2f}'.format(seno))
print('O cosseno é: {:.2f}'.format(cosseno))
print('A tangente é: {:.2f}'.format(tangente))
