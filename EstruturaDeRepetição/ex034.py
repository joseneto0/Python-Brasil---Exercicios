numero = int(input('Digite um número: '))
if numero > 1:
    for i in range(2, numero):
        if numero % i == 0:
            print('O número não é primo :c')
            break
    else:
        print('O número é primo :D')
else:
    print('O número não é primo')