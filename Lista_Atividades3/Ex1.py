def main():
    valor = int(input("Digite um valor: "))
    valores = []
    pares = []
    impares = []

    
    while valor != 0:
        valores.append(valor)
        valor = int(input("Digite um valor(Digite o valor 0 para parar): "))

    for v in valores:
        if v % 2 == 0:
            pares.append(v)
        else:
            impares.append(v)
        
    print("Pares: ", pares)
    print("Impares: ", impares)
    print("Total de Pares: ", len(pares))
    print("Total de Impares: ", len(impares))

main()