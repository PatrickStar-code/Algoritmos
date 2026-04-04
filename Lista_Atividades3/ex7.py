print("TABUADA")
numero = int(input("Digite um número para ver a tabuada até o número: "))
print(f"Tabuada do {numero}:")
for i in range(1, numero + 1):
    print(f"{numero} x {i} = {numero * i}")