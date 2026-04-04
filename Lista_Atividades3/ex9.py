n = int(input("Digite um número de valores a serem lidos: "))

def fatorial(num):
    for i in range(1, num):
        num *= i
    return num
        

for i in range(n):
    valor = int(input(f"Digite o {i + 1}º número: "))
    fatorial_valor = fatorial(valor)
    print(f"Valor lido: {valor} e seu fatorial é: {(fatorial_valor)}")