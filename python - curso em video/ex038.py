'''
Escreva um programa que leia dois números inteiros e 
compare-os, mostrando na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''
n1 = int(input('Primeiro: '))
n2 = int(input('Segundo:'))

if n1 > n2:
    print('O número {} é maior que {}'.format(n1, n2))
elif n1 == n2:
    print('O número {} é igual que {}'.format(n1, n2))
else:
    print('o número {} é maior que {}'.format(n2, n1))
