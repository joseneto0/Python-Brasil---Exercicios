n1, n2 = map(float, input('Digite suas 2 notas: ').split())
media = (n1 + n2) / 2
if media < 4.0:
    print('Média: {}\nREPROVADO - E'.format(media))
elif media >= 4 and media < 6:
    print('Média: {}\nREPROVADO - D'.format(media))
elif media >= 6 and media < 7.5:
    print('Média: {}\APROVADO - C'.format(media))
elif media >= 7.5 and media < 9.0:
    print('Média: {}\nAPROVADO - B'.format(media))
else:
    print('Média: {}\nAPROVADO - A'.format(media))