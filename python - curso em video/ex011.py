altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))
area = altura * largura
tinta = area / 2 
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m2'.format(altura, largura, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))