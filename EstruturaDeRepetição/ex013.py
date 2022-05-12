base = int(input('Qual sua base? '))
expoente = int(input('Qual seu expoente? '))
potencia = 1
for i in range(expoente):
    potencia *= base
    i += 1
print(f'{base} ^ {expoente} = {potencia}')