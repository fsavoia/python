# Desafio010
# ----------
# Escreva um programa que leia quanto dinheiro uma pessoa tem na 
# carteira e mostre quantos dólares ela pode comprar.

# Considere
# U$$1.00 = R$5.71

# limpar terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')

reais=float(input('Digite valor em reais: R$'))

grana=(reais/5.71)

print('\nVoce pode comprar U${:.2f} dólares com R${:.2f} reais.\n'.format(grana, reais))
print('Cotação atual do dólar: R$5,71.\n')

