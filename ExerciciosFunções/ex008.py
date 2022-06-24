def digitosNumero(numero):
    numero = str(numero)
    return len(numero)


num = int(input('Digite um número: '))
print(f'O número digitado tem {digitosNumero(num)} dígito(s)')