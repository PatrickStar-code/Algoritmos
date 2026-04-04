# Algoritmo para calcular E

def calcular_E(N):
    E = 1.0
    fatorial = 1
    for i in range(1, N+1):
        fatorial *= i
        E += 1 / fatorial
    return E

N = 1
while N > 0:
    N = int(input("Digite um valor inteiro e positivo N: "))

    if N > 0:
        resultado = calcular_E(N)
        print(f"O valor de E é sendo N={N}:  {resultado}")
    else:
        print("N deve ser um número inteiro positivo.")
