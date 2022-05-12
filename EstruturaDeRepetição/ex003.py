nome = input('Digite seu nome: ')
while len(nome) <= 3:
    nome = input('Digite seu nome: ')

idade = int(input('Digite sua idade: [0-150] '))
while idade < 0 or idade > 150:
    idade = int(input('Digite sua idade: [0-150] '))

salario = int(input('Digite seu salário: '))
while salario < 0:
    salario = int(input('Digite seu salário: '))

sexo = ('Digite seu sexo: [F/M] ')
while sexo not in 'FfMm':
    sexo = input('Digite seu sexo: [F/M] ')

estado_civil = input('Digite seu estado civil: [S/C/V/D] ')
while estado_civil not in 'SsCcVvDd':
    estado_civil = input('Digite seu estado civil: [S/C/V/D] ')