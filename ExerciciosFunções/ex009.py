def inversoNumero(numero):
    numero = str(numero)
    return numero[::-1]


#prog principal
num = int(input('Digite um número: '))
print(f'Número invertido: {inversoNumero(num)}')