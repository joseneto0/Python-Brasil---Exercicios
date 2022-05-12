numero = int(input('Que termo quer encontrar? '))
primeiro = 0
segundo = 1
fibo = 0
cont = 0
print(primeiro, end=' ')
for i in range(numero - 1):
    if i % 2 == 0:
        primeiro = fibo
    if i % 2 == 1:
        segundo = fibo
    fibo = primeiro + segundo
    cont += 1
    if cont < numero:
        print(fibo, end=' ')
    else:
        print(fibo)