n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
maior = max(n1, n2)
menor = min(n1, n2)

for i in range(menor, maior + 1):
    print(f"Limite inferior: {menor}, Limite superior: {maior}, Número atual: {i}")

    