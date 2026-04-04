valor = 0
total = 0
contador = 0

while valor >= 0:
    valor = float(input("Digite um número : "))
    total += valor
    contador += 1

media = total/contador
print(f"A mêdia aritmétrica é de : {media}")

