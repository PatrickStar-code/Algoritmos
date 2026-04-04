Candidato1 = 0
Candidato2 = 0
Candidato3 = 0
Candidato4 = 0
nulos = 0
brancos = 0
valor  = 1


while valor != 0:
    print("Votação: ")
    print("1 - Candidato 1")
    print("2 - Candidato 2")
    print("3 - Candidato 3")
    print("4 - Candidato 4")
    print("5 - Nulo")
    print("6 - Branco")
    print("0 - Encerrar votação")
    valor = int(input("Digite o número do candidato ou opção: "))

    if valor == 1:
        Candidato1 += 1
        print("Voto registrado para Candidato 1.")
    elif valor == 2:    
        Candidato2 += 1
        print("Voto registrado para Candidato 2.")
    elif valor == 3:
        Candidato3 += 1
        print("Voto registrado para Candidato 3.")
    elif valor == 4:
        Candidato4 += 1
        print("Voto registrado para Candidato 4.")
    elif valor == 5:
        nulos += 1
        print("Voto registrado para Nulo.")
    elif valor == 6:
        brancos += 1
        print("Voto registrado para Branco.")
    elif valor == 0:
        print("Votação encerrada.")
    else:
        print("Opção inválida. Tente novamente.")

total_votos = Candidato1 + Candidato2 + Candidato3 + Candidato4 + nulos + brancos 
print(f"Total de votos: {total_votos}")
print(f"Candidato 1: {Candidato1} votos")
print(f"Candidato 2: {Candidato2} votos")
print(f"Candidato 3: {Candidato3} votos")
print(f"Candidato 4: {Candidato4} votos")   
print(f"Nulos: {nulos} votos")
print(f"Brancos: {brancos} votos")