# Desafio032
# Faça um programa que leia um ano e mostre se é BISSEXTO

# atenção, o programa propositalmente não tem a lógica para identificar se o usuário
# digitou texto ao invés do número, esse lógica tem nos exercícios anteriores

# limpar terminal
from os import system, name
system('cls' if name == 'nt' else 'clear')

ano = input('Informe um ano: ')
zero = ano.endswith('00')

if zero == True:
    if int(ano) % 400 == 0:
        print(f'\nO ano {ano} é bissexto')
    else:
        print(f'\nO ano {ano} não é bissexto')
else:
    if int(ano) % 4 == 0:
        print(f'\nO ano {ano} é bissexto') 
    else:
        print(f'\nO ano {ano} não é bissexto')
