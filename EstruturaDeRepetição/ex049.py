n = int(input('Quantos termos? '))
cima = 1
baixo = 1
soma = 0
for i in range(n):
    S = cima / baixo
    cima += 1
    baixo += 2
    soma += S
print(f'S = {soma:.1f}')