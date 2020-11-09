# Desafio033
# Faça um programa que leia 3 números, mostre qual é o maior e qual é o menor

# limpar terminal
from os import system, name
system('cls' if name == 'nt' else 'clear')

n1 = int(input('Informe número 1: '))
n2 = int(input('Informe número 2: '))
n3 = int(input('Informe número 3: '))

# Verificando que é maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

# Verificando que é menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print(f'\nO maior número informado é {maior} e o menor é {menor}')
    