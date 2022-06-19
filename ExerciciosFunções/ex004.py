def verificaPositivo(num):
    if num > 0:
        return 'P'
    else:
        return 'N'


numero = int(input('Digite um número: '))
print(verificaPositivo(numero))