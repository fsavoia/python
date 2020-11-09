# Desafio019
# ----------
# Um professor quer sortear um dos seus quatros alunos para apagar o
# quadro. Faça um programa que ajude ele, lendo o nome deles e escevendo
# o nome do escolhido

# limpar terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')

#import random
from random import choice

nome1 = input('Digite o aluno 1: ')
nome2 = input('Digite o aluno 2: ')
nome3 = input('Digite o aluno 3: ')
nome4 = input('Digite o aluno 4: ')
lista = [nome1, nome2, nome3, nome4]
lista_final = choice(lista)

print(f'\nO sorteado foi: {lista_final}\n')
