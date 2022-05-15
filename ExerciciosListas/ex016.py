lista = []
salario = []
while True:
    vendas = int(input('Qual o valor das vendas brutas da semana? [0 para encerrar] '))
    salario.append(200 + (vendas * 9/100))
    lista.append(vendas)
    if vendas == 0:
        break
lista.remove(0)
for i in range(len(lista)):
    print(f'Salário {i+1}° - {salario[i]}')