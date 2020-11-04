# Desafio 008
# ----------
# Escreva um programa que leia um valor em metros e o
# exiba convertido em centímetros e milímetros

# limpar terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')

mt=float(input('Informe um valor em metros: '))

cent=(mt*100)
mili=(mt*1000)

print(f'\n{mt:.2f}m equivale a: {cent:.2f}cm')
print(f'{mt:.2f}m equivale a: {mili:.2f}mm\n')
