numero_alto = numero_baixo = altura_maior = altura_menor = 0
for i in range(10):
    numero_alunos = int(input(f'Código do aluno {i+1}: '))
    altura = float(input(f'Altura do aluno {i+1}: '))
    if i == 0:
        numero_alto = numero_baixo = numero_alunos
        altura_maior = altura_menor = altura
    else:
        if altura > altura_maior:
            altura_maior = altura
            numero_alto = numero_alunos
        elif altura < altura_menor:
            altura_menor = altura
            numero_baixo = numero_alunos
print('-=' * 20)
print(f'O aluno de número {numero_alto} possui a maior altura da turma, {altura_maior} m')
print(f'O aluno de número {numero_baixo} possui a menor altura da turma, {altura_menor} m')