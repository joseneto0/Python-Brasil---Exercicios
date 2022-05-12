numeros_pares = numeros_impares = 0
for i in range(1, 11):
    numeros = int(input(f'Digite o {i}° valor: '))
    if numeros % 2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1
print(f'Tem {numeros_pares} pares e {numeros_impares} ímpares')