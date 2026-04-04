positivo = 0
negativo = 0
contador = 0
valor = 1
total = 0
while valor != 0:
    valor = int(input("Digite um número (0 para encerrar): "))
    if valor > 0:
        positivo += 1
        contador += 1

    elif valor < 0:
        negativo += 1
        contador += 1

    total += valor

print(f"Total de números digitados: {contador}")
print(f"Total de números positivos: {positivo}")
print(f"Total de números negativos: {negativo}")
print(f"Media dos números digitados: {total / contador }")
