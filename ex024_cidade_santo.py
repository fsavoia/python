# Desafio024
# ----------
# Crie um programa que leia o nome de uma cidade
# e diga se ela começa ou não com o nome "SANTO"

# limpar terminal
from os import system, name
system('cls' if name == 'nt' else 'clear')

cidade = input('Digite o nome de uma cidade: ').strip().upper().replace( '-' , ' ' ).split()
print(cidade[0] == 'SANTO')