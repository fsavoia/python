# Desafio025
# ----------
# Crie um programa que leia o nome de uma pessoa
# e diga se ela tem "SILVA" no nome

# limpar terminal
from os import system, name
system('cls' if name == 'nt' else 'clear')

nome = input('Digite o nome de uma uma pessoa: ').upper().strip()

print(f'Seu nome tem Silva? {"SILVA" in nome}')