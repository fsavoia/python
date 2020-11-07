# Desafio028
# Escreva um programa que faz o computador pensar em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido

# O programa deverá escrever na tela, se o usuário venceu ou perdeu

# limpar terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')

# importar módulos random / speep
import random, time

print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar ...')
print('-=-'*20)

num = input('Em qual número eu pensei? ')

computador = random.randrange(6) # Escolhendo um número inteiro aleatório entre 0-5

# Usando para validar se o usuário não digitou um texto ao invés do número
# Ele tenta converter o num em float, se der, joga True na variável res, se der erro,
# joga False na variável res
try :  
    float(num) 
    res = True
except : 
    res = False

# Se for True, ele converter para inteiro, checa se o número é maior que 5, caso positivo, ele 
# informa a mensagem e, sai com exit 1 (error code)
if res == True:
    num=int(num)
    if num > 5:
        print('\n> Número inválido! Digite um número entre <0-5>')
        exit(1)
    else: # Caso seja menor que 1, ele faz o teste efetivo do game.
        if num == computador:
            print('PROCESSANDO...')
            time.sleep(3)
            print(f'\nPARABÉNS! Você conseguiu me vencer!')
        else:
            print('PROCESSANDO...')
            time.sleep(3)
            print(f'\nGANHEI! Eu pensei no número {computador} e não no número {num}.')
else: # Esse else é caso ele identifique que é um texto (False) 
    print('\n> Caractere inválido!')
    exit(1)

