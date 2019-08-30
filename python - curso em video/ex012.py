preco = float(input('Digite o valor do produto? R$ '))
desconto = preco - (preco * 5/100)
print('O produto custava R${:.2f}, e na promoção com desconto e 5% vai custar R${:.2f}'.format(preco, desconto))

