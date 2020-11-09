# Desafio017
# ----------
# Crie um programa que leia o comprimento do cateto oposto e
# do cateto adjacente de um triângulo, calcule e mostre o
# comprimento da hipotenusa

# limpar terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')

import math

cat_oposto = float(input('\nInforme o cateto oposto do triângulo: '))
cat_adjacente = float(input('Informe o cateto adjacente do triângulo: '))

# método math
hipotenusa = math.pow(cat_oposto,2)+math.pow(cat_adjacente,2)
print('\nA hipotenusa do triângulo é {:.2f}.'.format(math.sqrt(hipotenusa)))
print('\nA hipotenusa do triângulo é {:.2f}.'.format(math.hypot(cat_adjacente, cat_oposto)))

# método tradicional
hi = (cat_oposto ** 2 + cat_adjacente ** 2) ** (1/2)
print('\nA hipotenusa do triângulo é {:.2f}.'.format(hi))