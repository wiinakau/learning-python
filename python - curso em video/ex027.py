'''
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente

Ex: João Santana de Oliveira
primeiro = João
último = Oliveira
'''

nome = str(input('Digite o nome: ')).strip()
splitted = nome.split()
print('Seu primeiro nome é {}.'.format(splitted[0]))
print('Seu último nome é {}.'.format(splitted[-1]))


