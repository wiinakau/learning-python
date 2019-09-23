'''
Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:

-1 para binário
-2 para octal
-3 para hexadecimal
'''

numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Converter para Binário
[2] Converter para Octal
[3] COnverter para Hexadecimal
''')
opcao = int(input('Opção: '))
if opcao == 1:
    print('{} convertido para Binário é igual a {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para Octal é igual a {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção Inválida!')