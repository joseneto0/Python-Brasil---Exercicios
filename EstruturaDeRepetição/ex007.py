maior = 0
for i in range(5):
    numeros = int(input(f'Digite o {i}° valor: '))
    if numeros > maior:
        maior = numeros
    elif maior > numeros:
        maior = maior
print(f'O maior número é o {maior}')