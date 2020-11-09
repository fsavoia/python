valor=input('Digite algo: ')

print(f'''
O tipo de valor digitado é: {type(valor)}
O valor digitado é alfa-numérico? {valor.isalnum()}
O valor digitado é numérico? ' {valor.isnumeric()}
O valor digitado é todo minúsculo? {valor.islower()}
O valor digitado é todo maiúsculo? {valor.isupper()}'''
)