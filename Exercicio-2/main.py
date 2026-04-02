carga = 0
pesoMaximo = 5000 
itens = []

while True:
    print("Gerenciamento de Carga: ")
    print(" PESO LIVRE CAMINHÃO (KG) ")
    pesoAtual = pesoMaximo - carga
    print(pesoAtual)
    print("Qtde Itens Carregados")
    print(len(itens))
    print("1 - Adicionar Carga")
    print("2 - Mostrar itens")
    print("0 - Sair ")

    
    escolha = int(input(" Digite a Opção : "))


    if(escolha == 1 ):
        nome = input("Coloque o nome do produto: ")
        peso = float(input("Digite o peso em kg "))
        if(peso == 0): 
            print("Peso menor ou igual a 0 invalido")
        elif(peso > pesoAtual):
           print(" Não é possivel adicionar o item devido o peso ")
        else:
            carga += peso
            novoItem =  {nome,peso}
            itens.append(novoItem)
            print("Item adicionado - " + nome)
    elif(escolha == 2):
        print(itens)
    elif(escolha == 0):
        break

