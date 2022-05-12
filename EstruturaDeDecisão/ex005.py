n1, n2 = map(int, input('Digite 2 notas: ').split())
media = (n1 + n2) / 2
if media == 10:
    print('Parabéns, você foi aprovado com distinção!')
elif media >= 7:
    print('Parabéns, você foi aprovado')
else:
    print('Você foi reprovado :/')