


def Exercicio3():    
    contador=0
    salario = 0
    while salario != -1:
        salario = float(input("Digite o salario: "))
    
        if salario == -1:
            break
    
        numeroDeFilhos = int(input("Digite o numero de filhos: "))
        
        
        familias = []
        familias.append({"salario": salario, "numeroDeFilhos": numeroDeFilhos})
        
    print("Media de Salario da População")
    mediaSalario = 0
    for f in familias:
        mediaSalario += f["salario"]
    print(mediaSalario / len(familias))
    
    print("Media de Filhos da População")
    mediaFilhos = 0
    for f in familias:
        mediaFilhos += f["numeroDeFilhos"]
    print(mediaFilhos / len(familias))
    
    print("Maior Salario")
    maiorSalario = 0
    for f in familias:
        if int(f["salario"]) > int(maiorSalario):
            maiorSalario = f["salario"]
    print(maiorSalario)
    
    print("Percentual de pessoas com salario até 100")
    PessoasComSalarioAte100 = 0.0
    salarioTotal = 0.0
    
    for f in familias:
        if int(f["salario"]) <= 100:
            PessoasComSalarioAte100 += 1
            salarioTotal += f["salario"]
        salarioTotal += f["salario"]
        
        
    print("Media de Familias com salario de até 100 reais: " + str(PessoasComSalarioAte100 / salarioTotal))
    
        
        
        

if __name__ == "__main__":
    Exercicio3()