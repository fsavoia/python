# Desafio020
# ----------
# Um professor quer sortear a ordem de apresentação dos alunos.
# Faça um programa que leia o nome dos quatros alunos e mostre 
# a ordem sorteada

# limpar terminal
from os import system, name
system('cls' if name == 'nt' else 'clear')

import random

nome1 = input('Digite o aluno 1: ')
nome2 = input('Digite o aluno 2: ')
nome3 = input('Digite o aluno 3: ')
nome4 = input('Digite o aluno 4: ')

lista = [nome1, nome2, nome3, nome4]

random.shuffle(lista)
print(f'\nA ordem de apresentação de trabalho será: {lista}\n')