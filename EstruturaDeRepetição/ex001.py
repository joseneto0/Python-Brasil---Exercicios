nota = int(input('Digite uma nota: [0/10] '))
while nota < 0 or nota > 10:
    nota = int(input('Tente Novamente. Digite uma nota: [0/10] '))
print(f'Nota digitada: {nota}')