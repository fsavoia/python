# limpar terminal
from os import system, name
system('cls' if name == 'nt' else 'clear')

n1 = input('Digite a nota 1: ')

try :  
    float(n1) 
    res = True
except : 
    res = False

if res == True:
    n1=float(n1)
    if n1  > 10:
        print('> Nota 1 inválida! Nota válida: <0-10>')
        exit(1)
else:
    print('> Nota 1 inválida! Nota válida: <0-10>')
    exit(1)

n2 = input('Digite a nota 2: ')

try :  
    float(n2) 
    res2 = True
except : 
    res2 = False

if res2 == True:
    n2=float(n2)
    if n2  > 10:
        print('> Nota 2 inválida! Nota válida: <0-10>')
        exit(1)

else:
    print('> Nota 2 inválida! Nota válida: <0-10>')
    exit(1)

media = float((n1+n2)/2)
print(f'\nA média é: {media:.2f}')