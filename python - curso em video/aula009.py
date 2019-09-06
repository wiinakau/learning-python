frase = 'Learning Python pelo Youtube!'

# Fatiamento de string
print(frase[:5]) # começa do caractere zero
print(frase[6:]) # começa no 6 até o último caractere
print(frase[4:12])
print(frase[::2]) #[inicio:fim:passo]
print(frase[::-2]) #[inicio:fim:passo] invertido
print(frase[9::3]) # Inicia no caractere 9 de passo 3

# Análise de Strings
print(len(frase)) # Comprimento da Frase
print(frase.count('n')) # Contar quantas vezes aparece a letra 'n'
print(frase.count('n', 0, 7)) # Conta quantidade de 'o' no fatiamento de 0 a 7
print(frase.find('Py')) # Retorna a posição fatiamento 9
print(frase.find('café')) # Se não existim a string o retorno será -1
print('Python' in frase) # Retorna True

# Transformação
print(frase.replace('Python', 'Javascript!'))
print(frase.lower()) # Minúsculo
print(frase.upper()) # Maiúsculo
print(frase.capitalize()) # Transforma tudo em minúsulo depois coloca a primeira palavra em maiúsculo
print(frase.title()) # Transforma a primeira letra das palavras em maiúscula
print(frase.strip()) # Remove todos os espaços a direita e esquerda
print(frase.rstrip()) # Remove os caracteres a direita
print(frase.lstrip()) # Remove os caracteres a esquerda

#Divisão
print(frase.split()) # Divide a string pelos espaços gerando uma lista

#Junção
splitted = frase.split()
print('---'.join(splitted))

Ipsum = '''
Lorem Ipsum é simplesmente uma simulação de texto da indústria tipográfica e de impressos,
e vem sendo utilizado desde o século XVI, quando um impressor desconhecido pegou uma bandeja de tipos e os 
embaralhou para fazer um livro de modelos de tipos. Lorem Ipsum sobreviveu não só a cinco séculos, como 
também ao salto para a editoração eletrônica, permanecendo essencialmente inalterado. Se popularizou na 
década de 60, quando a Letraset lançou decalques contendo passagens de Lorem Ipsum, e mais recentemente 
quando passou a ser integrado a softwares de editoração eletrônica como Aldus PageMaker.
'''

print(Ipsum.count('A'))
print(Ipsum.find('A'))
print(len(Ipsum.split()))
print(Ipsum.lower().find('ipsum'))

print(Ipsum.split())
print(Ipsum.split()[1][3]) # Mostra o terceiro caractere de Ipsum