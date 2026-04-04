valor = 1
pares = 0
impares = 0
contador_pares = 0
contador_geral = 0
while valor != 0:
    valor = int(input("Digite um número (0 para encerrar): "))
    if valor % 2 == 0 and valor != 0:
        pares += valor
        contador_pares += 1
    elif valor % 2 != 0:
        impares += valor
    if valor != 0:
        contador_geral += 1
print(f"Media de números digitados: {((pares + impares) / contador_geral):.2f}")
print(f"Media de números pares: {(pares / contador_pares):.2f}")
print(f"Soma dos números pares: {pares}")
print(f"Soma dos números ímpares: {impares}")
print(f"Total de números pares digitados: {contador_pares}")
print(f"Total de números ímpares digitados: {contador_geral - contador_pares}")
