altura = float(input('Digite a altura: '))
formula_homens = (72.7 * altura) - 58
formula_mulheres = (62.1 * altura) - 44.7
print('O peso ideal para homens: {:.1f} kg\nO peso ideal para mulheres: {:.1f} kg'.format(formula_homens, formula_mulheres))