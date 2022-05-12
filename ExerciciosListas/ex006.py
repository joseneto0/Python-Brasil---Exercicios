lista = []
aprovados = 0
while True:
    nome = input('Digite o nome do aluno: ')
    nota_1 = float(input('Digite a 1° nota: '))
    while nota_1 < 0 or nota_1 > 10:
        nota_1 = float(input('Digite a 1° nota: [0-10] '))
    nota_2 = float(input('Digite a 2° nota: '))
    while nota_2 < 0 or nota_2 > 10:
        nota_2 = float(input('Digite a 2° nota: [0-10] '))
    nota_3 = float(input('Digite a 3° nota: '))
    while nota_3 < 0 or nota_3 > 10:
        nota_3 = float(input('Digite a 3° nota: [0-10] '))
    nota_4 = float(input('Digite a 4° nota: '))
    while nota_4 < 0 or nota_3 > 10:
        nota_4 = float(input('Digite a 4° nota: [0-10] '))
    media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
    if media >= 7.0:
        aprovados += 1
    lista.append([nome, [nota_1, nota_2, nota_3, nota_4], media])
    if len(lista) == 10:
        break
print('-=' * 30)
print(f'Tivemos {len(lista)} alunos cadastrados')
print(f'Tivemos {aprovados} alunos aprovados!')