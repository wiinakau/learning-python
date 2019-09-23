'''
Escreva um programa para aprovar o empréstimo bancário para a
compra de uma casa. O programa vai perguntar o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode
exceder 30% do salário ou então o empréstimo será negado.
'''

valor_casa = float(input('Qual o valo do imóvel: R$ '))
salario = float(input('Qual o salário: R$ '))
anos = int(input('Em quantos anos pretende pagar? '))

prestacao = valor_casa / (anos * 12)
valor_minimo = salario * (30/100)

print('Para pagar uma casa de R${:.2f} em {} anos'.format(valor_casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestacao))

if prestacao <= valor_minimo:
    print('O empréstimo foi Concedido!')
else:
    print('O empréstimo foi Negado!')