numeros = []
pares = []
impares = []
while True:
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    if len(numeros) == 10:
        break
print('-=' * 30)
print(f'Números: {numeros}')
pares.sort()
print(f'Pares: {pares}')
impares.sort()
print(f'Ímpares: {impares}')