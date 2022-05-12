notas = []
for i in range(1, 5):
    notas.append(float(input(f'Digite sua {i}° nota: ')))
print(f'Sua notas foram: {notas}')
print(f'Sua média foi: {sum(notas) / len(notas):.2f}')
