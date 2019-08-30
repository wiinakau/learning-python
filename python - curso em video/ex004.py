import math
# coding: utf-8
word = input('Digite algo: ')
print('Só tem espaços? ', word.isspace())
print('É um número? ', word.isnumeric())
print('É alfabético? ', word.isalpha())
print('É alfanúmerico?', word.isalnum())
print('É maiúsculas?', word.isupper())
print('É minúsculas?', word.islower())
print('É capitalizado?', word.istitle())