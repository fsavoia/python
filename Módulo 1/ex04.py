valor=input('Digite algo: ')
print('O tipo de valor digitado é: ', type(valor))
print('O valor digitado é alfabético? ', valor.isalpha())
print('O valor digitado é alfa-numérico? ', valor.isalnum())
print('O valor digitado é numérico? ', valor.isnumeric())
print('O valor digitado é todo maiúsculo? ', valor.isupper())
print('O valor digitado é todo minúsculo? ', valor.islower())
print('O valor digitado é somente espaço? ', valor.isspace())