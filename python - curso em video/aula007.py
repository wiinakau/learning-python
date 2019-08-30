#Operadores

nome = input('Qual o seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
d1 = n1 // n2
e = n1 ** n2
print('A soma é {}, \no produto é {}, \ne a divisão é {:.3f}'.format(s, m, d), end=' ') #não quebra a linha
print('Divisão inteira {} e potência {}'.format(d1, e))