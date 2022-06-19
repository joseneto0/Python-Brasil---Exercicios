def numeros(n):
    for i in range(n):
        i += 1
        print(str(i) * i)


#prog princip
n = int(input('Digite o número: '))
numeros(n)