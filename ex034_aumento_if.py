# Desafio034
# Faça um programa que pergunte o salário de um funionário e calcule o valor do seu aumento
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para salários inferiores ou iguais, o aumento é de 15%.

# limpar terminal
from os import system, name
system('cls' if name == 'nt' else 'clear')

salario = input('Informe o salário recebido R$: ').replace(',','.')
salario = float(salario)

if salario > 1250:
    aumento = salario+(salario*10/100)
else:
    aumento = salario+(salario*15/100)

print(f'\nO seu novo salário será de R$ {aumento:.2f}')