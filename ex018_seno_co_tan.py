# Desafio018
# ----------
# Crie um programa que leia um ângulo qualquer e mostre na tela 
# o valor do seno, cosseno e tengente desse ângulo

# limpar terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')

import math

ang = float(input('Digite o ângulo: '))

cose = math.cos(math.radians(ang))
seno = math.sin(math.radians(ang))
tang = math.tan(math.radians(ang))


print(f'\nO valor do Cosseno do ângulo {ang} é {cose}')
print(f'O valor do Seno do ângulo {ang} é {seno}')
print(f'O valor da Tangente do ângulo {ang} é {tang}\n')
