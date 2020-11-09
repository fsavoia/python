# Desafio009
# ----------
# Escreva um programa que leia um valor inteiro qualquer e
# mostre na tela a sua tabuada

# limpar terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')

num=int(input('Digite um número para ver sua tabuada: '))

print(f'''
{num}x0={num*0}
{num}x1={num*1}
{num}x2={num*2}
{num}x3={num*3}
{num}x4={num*4}
{num}x5={num*5}
{num}x6={num*6}
{num}x7={num*7}
{num}x8={num*8}
{num}x9={num*9}
{num}x10={num*10}
''')