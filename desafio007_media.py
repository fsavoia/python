# Desafio007
# ----------
# Desenvolva um programa que leia as notas
# de um aluno, calcule e mostre sua média

# limpar terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')

print('''
# ---------------------------------- #
# Calculando Média de Notas do Aluno #
# ---------------------------------- #
''')
nome=input('Nome do aluno: ')
nota1=float(input('Nota da prova 1 (0 -> 10): '))
nota2=float(input('Nota da prova 2 (0 -> 10): '))
media=(nota1+nota2)/2
print(f'\nA média do aluno {nome} é {media:.1f}\n')