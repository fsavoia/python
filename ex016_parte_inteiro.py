# Desafio016
# ----------
# Crie um programa que leia um número real qualquer e mostre na tela 
# a sua poção inteira
#
# Ex.:
# Digite um número: 6.127
# O número 6.127 tem a parte inteira 6

# limpar terminal
import os
import math

os.system('cls' if os.name == 'nt' else 'clear')
num = float(input('Informe um número real: '))

# resolvendo usando math.floor
num_int = math.floor(num)
print('\n# Método math.floor\nO número {} tem a parte inteira {}.'.format(num, num_int))

# resolvendo usando math.trunc
print('\n# Método math.trunc\nO número {} tem a parte inteira {}.'.format(num, math.trunc(num)))

# resolvendo usando conversão de variável
print(f'\n# Método usando conversão\nO número {num} tem a parte inteira {int(num)}\n')

