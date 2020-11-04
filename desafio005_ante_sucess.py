# - Desafio 005
# Faça um programa que leia um número inteiro e mostre
# na tela o seu sucessor e seu antecessor

# limpar terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')

num=int(input('Informe um número: '))
ant=num-1
suc=num+1

print('O número informado foi {}!\nSeu antecessor é {} e seu sucessor é {}'.format(num, ant, suc))
