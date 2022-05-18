gab = ''
certos = [] # recebe os acertos de todos
print('Digite o gabarito da prova: ')
for g in range(1, 11):
    gabarito = input(f'{g}° Questão: ').upper().strip()
    while gabarito not in 'ABCDE':
        gabarito = input(f'Digite um caracter válido. {g}° Questão: ').upper()
    gab += gabarito
acertos = 0
while True:
    print('-=' * 20)
    for i in range(1, 11):
        alunos = input(f'{i} - Digite sua resposta: ')
        while alunos not in 'ABCDE':
            alunos = input(f'Digite um caracter válido. {i} - Digite sua resposta: ')
        if i == 1 and alunos == gab[0]: #CONTINUAR AQUI
            acertos += 1
        elif i == 2 and alunos == gab[1]:
            acertos += 1
        elif i == 3 and alunos == gab[2]:
            acertos += 1
        elif i == 4 and alunos == gab[3]:
            acertos += 1
        elif i == 5 and alunos == gab[4]:
            acertos += 1
        elif i == 6 and alunos == gab[5]:
            acertos += 1
        elif i == 7 and alunos == gab[6]:
            acertos += 1
        elif i == 8 and alunos == gab[7]:
            acertos += 1
        elif i == 9 and alunos == gab[8]:
            acertos += 1
        elif i == 10 and alunos == gab[9]:
            acertos += 1    
    certos.append(acertos) 
    acertos = 0 
    continuar = input('Quer continuar? [S/N] ').upper()
    while continuar not in 'SN':
        continuar = input('Tente Novamente. Quer continuar? [S/N] ').upper()
    if continuar in 'N':
        break
print('-=' * 20)
print(certos)
print(f'O aluno {certos.index(min(certos))} acertou {min(certos)} questões, sendo a menor quantidade')
print(f'O aluno {certos.index(max(certos))} acertou {max(certos)} questões, sendo a maior quantidade')
print(f'No total, {len(certos)} alunos utilizaram o sistema')
print(f'A média total das notas dos alunos foi de {sum(certos) / len(certos):.1f}')