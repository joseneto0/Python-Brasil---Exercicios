frase = input('Digite uma frase: ').lower()
espaço = ' '
count_espaco = 0
vogais = 'aeiou'
count_vogais = 0
for i in range(len(frase)):
    if frase[i] in espaço:
        count_espaco += 1
    if frase[i] in vogais:
        count_vogais += 1
print(f'Na frase tem {count_espaco} espaços e {count_vogais} vogais')