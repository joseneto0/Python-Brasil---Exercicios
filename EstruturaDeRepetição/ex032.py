fatorial = int(input('Fatorial de: '))
multiplicacao = 1
print(f'{fatorial}! = ',end=' ')
while fatorial != 0:
    if fatorial > 1:
        print(f'{fatorial} .',end=' ')
    else:
        print(f'1',end=' ')
    multiplicacao *= fatorial
    fatorial -= 1
print(f'= {multiplicacao}',end=' ')