def main():
    contador = 0
    valores = []

    while contador < 20:
        valor = int(input("DIgite um valor: "))
        valores.append(valor)
        contador += 1

        
    maior = valores[0]
    menor = valores[0]
    
    for v in valores:
        if v > maior:
            maior = v
        if v < menor:
            menor = v
    
    print("Maior: ", maior)
    print("Menor: ", menor)

main()