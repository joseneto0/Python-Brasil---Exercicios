primos = []
numero = int(input('Digite o número: '))
for i in range(numero+1):
    if i % 2 == 1 and i != 2:
        primos.append(i)
print(f"Os números primos existentes entre 1 e {numero} são: ")
print(primos)