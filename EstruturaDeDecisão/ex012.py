ganho_hora = float(input('Quanto você ganha por hora? '))
horas_trabalhadas = int(input('Quantas horas você trabalha no mês? '))
salario_bruto = ganho_hora * horas_trabalhadas
if salario_bruto <= 900:
    inss = salario_bruto * 10/100
    salario_liquido = salario_bruto - inss 
    print('+ Salário Bruto : R$ {:.2f}'.format(salario_bruto))
    print('- IR (0%) : R$ 0.00')
    print('- INSS (8%) : R$ {:.2f}'.format(inss))
    print('FGTS (11%): R$ {:.2f}'.format(salario_bruto * 11/100))
    print('Total de descontos : R$ {:.2f}'.format(inss))
    print('= Salário Liquido : R$ {:.2f}'.format(salario_liquido))
elif salario_bruto <= 1500:
    inss = salario_bruto * 10/100
    imposto_de_renda = salario_bruto * 5/100
    salario_liquido = salario_bruto - imposto_de_renda - inss
    total_descontos = inss + imposto_de_renda
    print('+ Salário Bruto : R$ {:.2f}'.format(salario_bruto))
    print('- IR (5%) : R$ {:.2f}'.format(imposto_de_renda))
    print('- INSS (8%) : R$ {:.2f}'.format(inss))
    print('FGTS (11%) : R$ {:.2f}'.format(salario_bruto * 11/100))
    print('Total de descontos : R$ {:.2f}'.format(total_descontos))
    print('= Salário Liquido : R$ {:.2f}'.format(salario_liquido))
elif salario_bruto <= 2500:
    inss = salario_bruto * 10/100
    imposto_de_renda = salario_bruto * 10/100
    salario_liquido = salario_bruto - imposto_de_renda - inss
    total_descontos = inss + imposto_de_renda 
    print('+ Salário Bruto : R$ {:.2f}'.format(salario_bruto))
    print('- IR (10%) : R$ {:.2f}'.format(imposto_de_renda))
    print('- INSS (8%) : R$ {:.2f}'.format(inss))
    print('Total de descontos : R$ {:.2f}'.format(total_descontos))
    print('= Salário Liquido : R$ {:.2f}'.format(salario_liquido))
elif salario_bruto > 2500:
    inss = salario_bruto * 10/100
    imposto_de_renda = salario_bruto * 20/100
    salario_liquido = salario_bruto - imposto_de_renda - inss 
    total_descontos = inss + imposto_de_renda
    print('+ Salário Bruto : R$ {:.2f}'.format(salario_bruto))
    print('- IR (20%) : R$ {:.2f}'.format(imposto_de_renda))
    print('- INSS (8%) : R$ {:.2f}'.format(inss))
    print('Total de descontos : R$ {:.2f}'.format(total_descontos))
    print('= Salário Liquido : R$ {:.2f}'.format(salario_liquido))