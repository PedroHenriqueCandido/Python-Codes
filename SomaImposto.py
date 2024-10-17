def somaImposto (taxaImposto, custo):
    valorAlterado = (taxaImposto/100 * custo) + custo
    print(f"O valor com a taxa de imposto será: {valorAlterado}")

a = float(input("Digite a taxa de imposto: "))
b = float(input("DIgite o preço de custo: "))

somaImposto(a,b)