ganho_hora = float(input('Quanto você ganha por hora? '))
horas_trabalhadas = float(input('Quantas horas você trabalha por mês? '))
salario = ganho_hora * horas_trabalhadas
print('Seu salário é de R$ {:.2f}'.format(salario))