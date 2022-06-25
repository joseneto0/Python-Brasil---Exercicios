nome = input('Nome: ')
cont = len(nome)
for i in range(cont):
    print(nome[:cont].upper())
    cont -= 1