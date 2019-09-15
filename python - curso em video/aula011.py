# cores no terminal

print('\033[0;30;41mOlá, Mundo!\033[m')
print('\033[4;33;44mOlá Mundo\033[m')
print('\033[1;35;43mOlá Mundo\033[m')
print('\033[30;42mOlá Mundo\033[m')
print('\033[mOlá Mundo\033[m')
print('\033[7;30mOlá Mundo\033[m')

cores = {'limpa': '\033[m',
        'azul': '\033[34m',
        'amarelo': '\033[33m',
        'pretoebranco': '\033[7:30m'}

nome = 'Willian'
print('Olá! Muito prazer em te conhecer, {}{}{}!'.format(cores['amarelo'], nome, cores['limpa']))
