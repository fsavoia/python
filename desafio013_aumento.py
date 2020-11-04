# Desafio013
# ----------
# Escreva um programa que leia o salário do funcionário e mostre
# seu salário com 15% de aumento

# limpar terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')

salario=float(input('Informe o salário: R$'))

aumento=(salario+(salario*15/100))

print(f'\nO seu salário com 15% de aumento é: R${aumento:.3f}\n')