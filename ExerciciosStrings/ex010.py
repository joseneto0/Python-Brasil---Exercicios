from num2words import num2words
numero = int(input('Digite um número de 1 a 99: '))
while numero < 1 or numero > 99:
    numero = int(input('Tente Novamente. Digite um número de 1 a 99: '))
print(num2words(numero, lang='pt_BR'))