turmas = int(input('Quantas turmas tem? '))
soma = 0
for i in range(turmas):
    while True:
        alunos = int(input(f'Quantos alunos na {i+1}° turma? [máx-40] '))
        if alunos <= 40:
            break
    soma += alunos
media = soma / turmas
print(f'A média de alunos para cada turma é de {media}')