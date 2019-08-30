# coding: utf-8
# modúlos
# ceil
# floor
# trunc
# pow potência
# sqrt
# factorial
from math import sqrt, floor, ceil
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A rapuz de {} é igual a {:.2f}'.format(num, raiz))
print('A raíz de {} é igual a {}'.format(num, ceil(raiz)))  # arredonda pra cima
print('A raíz de {} é igual a {}'.format(num, floor(raiz)))  # a rrendonda para baixo
