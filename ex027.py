# Desafio027
# ----------
# Crie um programa que leia o nome completo de uma pessoa, mostrando
# em seguida o primeiro e o último nome separadamente.

# Ex.: Ana Maria de Souza
# primeiro = Ana
# último = Souza

# limpar terminal
from os import system, name
system('cls' if name == 'nt' else 'clear')

nome = input('Digite seu nome completo: ')
dividido = nome.split()

print('primeiro = {}'.format(dividido[0]))
print('último = {}'.format(dividido[]))
