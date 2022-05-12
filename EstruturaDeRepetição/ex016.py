while True:
    numero = int(input('Que termo quer encontrar? [0-500] '))
    if numero <= 500:
        break
primeiro = 0
segundo = 1
fibo = 0
print(primeiro, end=' ')
for i in range(numero - 1):
    if i % 2 == 0:
        primeiro = fibo
    if i % 2 == 1:
        segundo = fibo
    fibo = primeiro + segundo
    print(fibo, end=' ')