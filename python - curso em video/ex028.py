'''
Escreva um programa que faça o jogo "pensar" em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o
número escolhido pelo computador.

o programa deverá escrever na tela se o usuário venceu ou perdeu
'''

from random import randint

numero = randint(0, 5)
chance = int(input('Tente adivinhar o número: '))
print('Acertou' if numero == chance else 'Tente novamente')