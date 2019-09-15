'''
Escreva um programa que leia a velocidade de um carro

Se ele ultrapassar 80Km/h, mostre 
uma mensagem dizendo que ele foi multado

A multa vai custar R$7,00 por cada Km acima do limite
'''

velocidade = float(input('Qual a velocidade do carro: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você excedeu o limite permitido que é de 80Km/h')
    print('E será multado em R${:.2f}.'.format(multa))
else: 
    print('A velocidade do carro estava em {}Km/h e por isso não foi multado.'.format(velocidade))