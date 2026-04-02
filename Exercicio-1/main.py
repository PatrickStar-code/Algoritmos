salario = float(input("DIGITE SEU SALARIO : "))

if(salario < 0):
    print("Salario informado de forma incorreta")
elif(salario <= 5000):
    print("2% aplicado")
    novoSalario = salario * 1.02
    print(novoSalario)
else:
    print("5% aplicado")
    novoSalario = salario * 1.05
    print(novoSalario)