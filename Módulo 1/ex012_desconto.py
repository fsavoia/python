# Desafio012
# ----------
# Escreva um programa que leia o preço do produto e mostre
# seu desconto com 5%

# limpar terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')

produto=float(input('Informe o valor do produto: R$'))

tx_desc=(produto-(produto*5/100))

print(f'\nO produto com 5% de desconto sai por: R${tx_desc:.3f}\n')