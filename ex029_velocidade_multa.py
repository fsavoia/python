# Desafio029
# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele
# foi multado. A multa vai custar R$ 7,00 por cada KM acima do limite 

# limpar terminal
from os import system, name
system('cls' if name == 'nt' else 'clear')

import time

print('-=-'*20)
print('DETRAN-SP -- CÁLCULO DE VELOCIDADE')
print('-=-'*20)

velocidade = input('Digite a velocidade que o carro estava (km/h): ')

try :  
    int(velocidade) 
    res = True
except : 
    res = False

if res == True:
    velocidade=int(velocidade)
    if velocidade > 80:
        multa = (velocidade - 80) * 7
        print('Analisando...')
        time.sleep(3)
        print(f'\n<> Você estava acima do limite. Você deverá pagar R$ {multa} de multa.')
    else:
        print('Analisando...')
        time.sleep(3)
        print('\n>> Você estava na velocidade permitida.')
else: # Esse else é caso ele identifique que é um texto (False) 
    print('\n> Caractere inválido!')
    exit(1)