n1, n2, n3 = map(float, input('Digite suas 3 notas: ').split())
if (n1 + n2 + n3) / 3 >= 7.0 and (n1 + n2 + n3) / 3 < 10.0:
    print(f'Aprovado! \nSua média foi {(n1+n2+n3) / 3}')
elif (n1 + n2 + n3) / 3 < 7.0:
    print(f'Aprovado :c \nSua média foi {(n1+n2+n3) / 3}')
elif (n1 + n2 + n3) / 3 == 10:
    print(f'Aprovado com Distinção, você é um monstro! Sua média foi {(n1 + n2 + n3) / 3}')