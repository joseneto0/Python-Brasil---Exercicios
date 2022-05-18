notas = []
atleta = input('Atleta: ')
for i in range(7):
    n = float(input('Nota: '))
    notas.append(n)
print()
print('Resultado final:')
print(f'Atleta: {atleta}')
print(f'Melhor nota: {max(notas)}')
print(f'Pior nota: {min(notas)}')
notas.remove(max(notas))
notas.remove(min(notas))
print(f'Média: {sum(notas) / len(notas):.2f}')