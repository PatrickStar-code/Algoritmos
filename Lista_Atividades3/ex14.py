numeroInicial = 1000
numeroFinal = 1999

for numero in range(numeroInicial, numeroFinal + 1):
    if numero % 11 == 5:
        print(f"Número: {numero} é divisível por 11 e deixa resto 5")
