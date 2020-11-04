# Desafio 006
# -----------
# Crie um algoritmo que leia um número e mostre 
# o seu dobro, triplo e raiz quadrada

# limpar terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')

num=int(input('Digite um número: '))

#print('O dobro de {} é {} \nO triplo de {} é {} \nA raíz quadrada de {} é {:.2f}'.format(num, num*2, num, num*3, num, num**(1/2)))

d=num*2
t=num*3
rq=pow(num, (1/2))

print(f'''
O dobro de {num} é {d}
O triplo de {num} é {t}
A raíz quadrada de {num} é {rq:.2f}'''
)

