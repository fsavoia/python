# Desafio035
# Desenvolva um programa que leia o comprimento das três retas e diga ao usuário
# se elas podem ou não formar um triângulo

# limpar terminal
from os import system, name
system('cls' if name == 'nt' else 'clear')

import time

print('-=-'*9)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-'*9)

r1 = int(input('Informe a reta 1: '))
r2 = int(input('Informe a reta 2: '))
r3 = int(input('Informe a reta 3: '))

print('Analisando...')
time.sleep(3)

if r1+r2>r3 and r1+r3>r2 and r2+r3>r1:
    print('\nAs retas informadas podem ser um triângulo!!')
else:
    print('\nAs retas passadas não formam um triângulo!!')


