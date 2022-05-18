n = int(input('Quantos termos? '))
baixo = 2
for i in range(n):
    H = 1 + 1 / baixo
    baixo += 1
print(f'H = {H:.1f}')