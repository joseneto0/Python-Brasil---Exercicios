idades = []
alturas = []
qntd_alunos = 0
for i in range(5): #30
    idades.append(int(input(f'{i+1}° - Digite sua idade: ')))
    alturas.append(float(input(f'{i+1}° - Digite sua altura: ')))
media_altura = sum(alturas) / len(alturas)
for i in range(0, len(idades)):
    if idades[i] > 13 and alturas[i] < media_altura:
        qntd_alunos += 1
print(f'Média de altura: {media_altura:.2f}')
print(f'{qntd_alunos} alunos possuem altura menor que a média e tem mais de 13 anos')