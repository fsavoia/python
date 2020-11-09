# Desafio011
# ----------
# Escreva um programa que leia a largura e a atura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m quadrados

# limpar terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')

larg=float(input('Informe a largura da parede em metros: '))
alt=float(input('Informe a altura da parede em metros: '))
area=larg*alt
tinta=area/2

print ('')
print('-' * 50)
print(f'\nArea total possui {area}m quadrados, portanto você precisa de {tinta}l de tinta.\n')
