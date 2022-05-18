n = int(input('Quantos termos? '))
cima = 1
baixo = 1
soma = 0
print(f'S = ',end='')
for i in range(n):
    S = cima / baixo
    print(f'{cima}/{baixo} +',end=' ')
    cima += 1
    baixo += 2
    soma += S
print()
print(f'S = {soma:.1f}')
