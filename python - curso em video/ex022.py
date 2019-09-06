'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas
- O nome com todas minúsculas
- Quantas letras ao todo (sem os espaços)
- Quantas letras tem o primeiro nome
'''

nome_completo = input('Digite seu nome: ')
print('Maiúscula {}.'.format(nome_completo.upper()))
print('Minúscula {}.'.format(nome_completo.lower()))
print('O nome completo sem os espaços tem {}.' .format(len(nome_completo.replace(' ', ''))))
print('O primeiro nome tem {} letras.' .format(len(nome_completo.split()[0])))