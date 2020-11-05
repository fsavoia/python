# Desafio023
# ----------
# Crie um programa que leia o nome completo de uma pessoa e mostre
# - O nome com todas as letras maiúsculas
# - O nome com todas as letras minúsculas
# - Quantas letras ao todo (sem considerar espaços)
# - Quantas letras tem o primeiro nome

# limpar terminal
from os import system, name
system('cls' if name == 'nt' else 'clear')

nome = input('Digite seu nome completo: ').strip()
dividido = nome.split()

print('\n1 - O nome com todas as letras maiúsculas = ', nome.upper())
print('2 - O nome com todas as letras minúsculas = ', nome.lower())
print('3 - Quantas letras ao todo (sem considerar espaços) = ', len(nome) - nome.count(' '))
print('4 - Quantas letras tem o primeiro nome = ', len(dividido[0]))
