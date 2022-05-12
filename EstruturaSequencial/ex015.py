ganho_hora = float(input('Quanto você ganha por hora? '))
horas_trabalhadas = int(input('Quantas horas você trabalha no mês? '))
salario_bruto = ganho_hora * horas_trabalhadas
imposto_de_renda = salario_bruto * 11/100
inss = salario_bruto * 8/100
sindicato = salario_bruto * 5/100
salario_liquido = salario_bruto - imposto_de_renda - inss - sindicato
print('+ Salário Bruto : R$ {:.2f}'.format(salario_bruto))
print('- IR (11%) : R$ {:.2F}'.format(imposto_de_renda))
print('- INSS (8%) : R$ {:.2f}'.format(inss))
print('- Sindicato (5%) : R$ {:.2f}'.format(sindicato))
print('= Salário Liquido : R$ {:.2f}'.format(salario_liquido))