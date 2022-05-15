lista = []
lista.append(input('Telefonou para vítima? [S/N] ')) 
lista.append(input('Esteve no local do crime? [S/N] '))
lista.append(input('Mora perto da vítima? [S/N] '))
lista.append(input('Devia para a vítima? [S/N] '))
lista.append(input('Ja trabalhou com a vítima? [S/N] '))
if lista.count('S') == 0 or lista.count('S') == 1:
    print("Inocente")
elif lista.count('S') == 2:
    print("Suspeito")
elif lista.count('S') == 3 or lista.count('S') == 4:
    print('Cúmplice')
else:
    print("Assasino")