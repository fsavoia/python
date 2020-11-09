# Desafio022
# ----------
# Crie um programa que leia o um número de 0 - 9999 e mostre 
# na tela cada um dos digitos separados.
#
# Ex.: Digite um número: 1834
#
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

# limpar terminal
from os import system, name
system('cls' if name == 'nt' else 'clear')

num = int(input('Digite um número de 0-9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('\nunidade: ', u)
print('dezena: ', d)
print('centena: ', c)
print('milhar: ', m)