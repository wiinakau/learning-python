'''
Desenvolva um programa que pergunte a distância de uma viagem em KM.
Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de
até 200Km e R$0,45 para viagens mais longas.
'''

distancia = int(input('Qual a distância da viagem? '))
if distancia > 200:
    preco = distancia * 0.45
else:
    preco = distancia * 0.5

# preco = distancia * 0.45 if distancia > 200 else distancia * 0.45    
print('O preço da passagem será de R${:.2f}'.format(preco))