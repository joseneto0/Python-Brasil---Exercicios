string1 = input('String 1: ')
string2 = input('String 2: ')
print(f'Tamanho de "{string1}": {len(string1)} caracteres')
print(f'Tamanho de "{string2}": {len(string2)} caracteres')
if len(string1) != len(string2):
    print('As duas strings são de tamanhos diferentes.')
else:
    print('As duas strings são de mesmo tamanhos')
if string1 != string2:
    print('As duas strings possuem conteúdo diferente')
else:
    print('As duas strings tem o mesmo conteúdo')