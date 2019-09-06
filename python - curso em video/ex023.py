'''
Faça um programa que leia um número de 0 a 9999 e 
mostre na tela cada um dos dígitos separados
Ex: Digite um número: 1942

unidade: 2
dezena: 4
centena: 9
milhar: 1
'''
num = int(input('Digite um número de 0 a 9999: '))

unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print('Número: {}'.format(num))
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))

# num = int(input('Digite um número de 0 a 9999: '))
# num = str(num)
# unidade = num[3]
# dezena = num[2]
# centena = num[1]
# milhar = num[0]
# print('Número: {}'.format(num))
# print('Unidade: {}'.format(unidade))
# print('Dezena: {}'.format(dezena))
# print('Centena: {}'.format(centena))
# print('Milhar: {}'.format(milhar))