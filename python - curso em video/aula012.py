nome = str(input('Digite seu nome: '))
if nome == 'Willian':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular!')
elif nome in 'Ana Claúdia Jéssica Juliana':
    print('Belo nome!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))