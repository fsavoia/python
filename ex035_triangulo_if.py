# Desafio035
# Desenvolva um programa que leia o comprimento das três retas e diga ao usuário
# se elas podem ou não formar um triângulo

# limpar terminal
from os import system, name
system('cls' if name == 'nt' else 'clear')

import time

print('\033[1;33m-=-\033[m'*9)
print('\033[1mANALISADOR DE TRIÂNGULOS\033[m')
print('\033[1;33m-=-\033[m'*9)

r1 = int(input('Informe a reta 1: '))
r2 = int(input('Informe a reta 2: '))
r3 = int(input('Informe a reta 3: '))

print('Analisando...')
time.sleep(3)

if r1+r2>r3 and r1+r3>r2 and r2+r3>r1:
    print('\nAs retas informadas \033[1;32mpodem ser\033[m um triângulo!!')
else:
    print('\n\033[31mAs retas passadas não formam um triângulo!!\033[m')


