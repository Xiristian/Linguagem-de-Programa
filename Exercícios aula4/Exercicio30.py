valorReais   = float(input("Digite um valor em R$: "))
cotacaoDolar = float(input("Digite a cotaçao do dólar: "))
valorDolar   = valorReais * cotacaoDolar

print("O valor digitado em dólar é:", "%.2f" % (valorDolar), "US$")