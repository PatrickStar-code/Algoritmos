def main():
    familias = 0
    totalFilhos = 0
    maiorSalario = 0
    salarioAte100 = 0
    salarioTotal = 0
    salario = 0
    
    while salario != -1:
        salario = float(input("Digite o salario: "))

        if salario == -1:
            break
        
        numeroDeFilhos = int(input("Digite o numero de filhos: "))
            
        familias += 1
        totalFilhos += numeroDeFilhos
            
        if salario > maiorSalario:
            maiorSalario = salario
            
        if salario <= 100:
            salarioAte100 += 1
        salarioTotal+=salario
    
    mediaSalario = salarioTotal / familias
    mediaFilhos = totalFilhos / familias
    percentualSalarioAte100 = salarioAte100 / familias * 100
    
    print("Media de Salario: ", mediaSalario)
    print("Media de Filhos: ", mediaFilhos)
    print("Maior Salario: ", maiorSalario)
    print("Percentual de Salario ate 100: ", percentualSalarioAte100)
    
   
main()