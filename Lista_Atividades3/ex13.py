aumento = 0.20
precoProduto = 0
codigoProduto = 0

produtos = {}
while codigoProduto >= 0:
    codigoProduto = int(input("Digite o código do produto (ou um número negativo para sair): "))
    if(codigoProduto >= 0):
        precoProduto = float(input("Digite o preço do produto: "))
        if(precoProduto >= 0):
            precoAumentado = precoProduto + (precoProduto * aumento)
            print(f"Preço do produto com aumento: {precoAumentado:.2f}")
            if(codigoProduto in produtos):
                print("Código do produto já existe. Atualizando o preço.")
            produtos[codigoProduto] = [precoProduto, precoAumentado]
        else: 
            print("Não vendemos produtos com preço negativo ou igual a zero")

for codigo, precos in produtos.items():
    print(f"Código do produto: {codigo}, Preço original: {precos[0]:.2f}, Preço com aumento: {precos[1]:.2f}")
