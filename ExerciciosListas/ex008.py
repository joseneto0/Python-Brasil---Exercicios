idade = []
altura = []
for i in range(1, 6):
    idade.append(int(input(f'{i}° - Digite sua idade: ')))
    altura.append(float(input(f'{i}° - Digite sua altura: ')))
idade.reverse()
print(f'As idades em ordem reversa: {idade}')
altura.reverse()
print(f'As alturas em ordem reversa: {altura}')