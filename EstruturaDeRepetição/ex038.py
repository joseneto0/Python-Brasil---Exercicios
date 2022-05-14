from time import sleep
print('Um funcionário foi contratado em 1995, e seu salário inicial era de R$ 1000.00')
sleep(1)
print('Em 1996 ele recebeu aumento de 1.5% sobre o seu salário')
sleep(1)
print('A partir do ano 1997 ele passa a ganhar o dobro do aumento do ano anterior')
sleep(1)
print('Agora sua vez de participar da simulação :3')
salario_inicial = float(input('Qual o salário inicial? '))
ano_inicial = 1995
porcentagem = 0.015
ano_final = int(input('Até que ano você quer saber quanto ele vai ganhar? '))
print('-=' * 20)
print(f'No ano de 1995, você receberá R$ {salario_inicial:.2f}')
for i in range(ano_inicial, ano_final+1):
    if ano_inicial == 1996:
        salario = salario_inicial + (salario_inicial * porcentagem)
        print(f'No ano de {i}, você receberá R$ {salario:.2f}')
    elif ano_inicial == 1997:
        porcentagem_atual = porcentagem * 2
        porcentagem *= 2
        salario_final = salario + (salario * porcentagem_atual)
        print(f'No ano de {i}, você receberá R$ {salario_final:.2f}')
    elif ano_inicial >= 1998:
        porcentagem_atual = porcentagem * 2
        porcentagem *= 2
        salario_final = salario_final + (salario_final * porcentagem_atual)
        print(f'No ano de {i}, você receberá R$ {salario_final:.2f}')
    ano_inicial += 1
print('-=' * 20)