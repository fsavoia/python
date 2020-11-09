# Desafio030
# Escreva um programa que leia um número inteiro e mostre
# na tela se ele é par ou ímpar

# limpar terminal
from os import system, name
system('cls' if name == 'nt' else 'clear')

num = int(input('Informe um número: '))
res = num % 2

# atenção, o programa propositalmente não tem a lógica para identificar se o usuário
# digitou texto ao invés do número, esse lógica tem nos exercícios anteriores

if res == 0:
    print(f'\nO número {num} é PAR')
else:
    print(f'\nO número {num} é ÍMPAR')

