n = 1
valor = 0
while n > 0:
    valor = 0
    n = int(input("Digite um número (0 para encerrar): "))
    for i in range(1, n + 1):
        valor +=  1/i
    print(f"Número: {n}, Valor final: {valor:.2f}")
