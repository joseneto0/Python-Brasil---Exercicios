frase = input('Digite um nome/frase: ').strip().upper()
palavras = frase.split()
frase_junta = ''.join(palavras)
if frase_junta == frase_junta[::-1]:
    print('É um Palíndromo :D')
else:
    print('Não é um Palíndromo :C')