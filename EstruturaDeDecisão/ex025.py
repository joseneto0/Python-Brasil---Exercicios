print('-=' * 30)
print('                 PERGUNTAS SOBRE O CRIME')
print('-=' * 30)
participação = 0
telefone = input('Telefou para a vítima? [S/N] ')
if telefone in 'Ss':
    participação += 1
local = input('Esteve no local do crime? [S/N] ')
if local in 'Ss':
    participação += 1
mora = input('Mora perto da vítima? [S/N] ')
if mora in 'Ss':
    participação += 1
dever = input('Devia para a vítima? [S/N] ')
if dever in 'Ss':
    participação += 1
trabalhar = input('Já trabalhou com a vítima? [S/N] ')
if trabalhar in 'Ss':
    participação += 1
print(f'Você teve participação em {participação} ocorrências. ', end='')
if participação == 2:
    print('SUSPEITO!')
elif participação == 3 or participação == 4:
    print('CÚMPLICE!')
elif participação == 5:
    print('ASSASSINO!')
else:
    print('INOCENTE!')