valor = 1
positivos = 0
negativos = 0
while (valor != 0):
    valor = int(input("Digite um Valor: "))
    if (valor > 0):
        positivos = positivos + 1
    elif (valor < 0):
        negativos = negativos + 1
print(f"A quantidade de valores positivos é: {positivos}")
print(f"A quantidade de valores negativos é: {negativos}")
