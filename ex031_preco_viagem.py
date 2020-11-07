# Desafio031
# Escreva um programa que pergunte a distância de uma viagem
# em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km para
# viagens de até 200km e R$ 0,45 para viagens mais longas

# atenção, o programa propositalmente não tem a lógica para identificar se o usuário
# digitou texto ao invés do número, esse lógica tem nos exercícios anteriores

# limpar terminal
from os import system, name
system('cls' if name == 'nt' else 'clear')

import time

print('-=-'*20)
print('SAVOIA TRANSPORTES - VAMOS CALCULAR O PREÇO DA SUA VIAGEM')
print('-=-'*20)

distancia = int(input('Informe a distância de sua viagem (Km): '))
print('Calculando...')
time.sleep(3)

if distancia > 200:
    print(f'\nO valor da passagem sairá por R$ {float(distancia*0.45):.2f}')
else:
    print(f'\nO valor da passagem sairá por R$ {float(distancia*0.50):.2f}')

print('# Tenha uma boa viagem! Volte sempre!')