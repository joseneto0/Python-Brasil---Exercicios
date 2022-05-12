numero = int(input('Digite o número: '))
print(f'{numero}! = ',end='')
multiplicador = 1
for i in range(numero, 0, -1):
    print(f'{i}',end=' ')
    multiplicador *= i
print(f'= {multiplicador}')