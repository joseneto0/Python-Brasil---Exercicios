def somaImposto(taxa, custo):
    return custo + (custo * (taxa/100))

taxa = int(input('Digite a taxa de imposto: '))
custo = int(input('Digite o custo: '))
print(somaImposto(taxa, custo))