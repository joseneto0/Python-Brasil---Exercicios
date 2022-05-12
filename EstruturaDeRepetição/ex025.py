qntd_pessoas = 0
soma = 0
while True:
    pessoas = int(input('Quantos anos você tem? '))
    qntd_pessoas += 1
    soma += pessoas
    continuar = input('Quer continuar? [S/N] ')
    if continuar in 'Nn':
        break
    
media = soma / qntd_pessoas
if media >= 0 and media <= 25:
    print(f'A média de idades deu {media}, sua turma é Jovem!')
elif media > 25 and media <= 60:
    print(f'A média deu de idades deu {media}, sua turma é Adulta!')
else:
    print(f'A média deu de idades deu {media}, sua turma é Idosa!')