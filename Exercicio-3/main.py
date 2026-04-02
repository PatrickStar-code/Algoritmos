alturas = []

while True:
    print("Caso deseje sair digite 0 ou valor negativo")
        
    alturaAtual = float(input("Digite a altura en cm: "))
    if(alturaAtual > 0):
        print("Altura Adicionada ")
        alturas.append(alturaAtual)
    else:
        print("Programa Finalizado ")
        n = len(alturas)
        for i in range(n-1):
            swapped = False
            for j in range(n-i-1):
                if alturas[j] > alturas[j+1]:
                    alturas[j], alturas[j+1] = alturas[j+1], alturas[j]
                    swapped = True
            if not swapped:
                break
            
        sem_duplicatas = list(dict.fromkeys(alturas))
        print(sem_duplicatas[-3:])
        break
