# Desafio026
# ----------
# Crie um programa que leia o uma frase pelo teclado e mostre:
#
# - Quantas vezes aparece a letra "A"
# - Em que posição ela aparece a primeira vez
# - Em que posição ela aparece a última vez

# limpar terminal
from os import system, name
system('cls' if name == 'nt' else 'clear')

frase = input('Escreva uma frase: ').upper().strip()

print(f'\nA letra "A" aparece {frase.count("A")} vezes na sua frase')
print(f'A letra "A" aparece na posição {frase.find("A")+1} da sua frase')
print(f'A letra "A" aparece pela última vez na posição {frase.rfind("A")+1} da sua frase')
