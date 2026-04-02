valor = int(input("Digite um Valor: "))
soma = 0
contador = 0

while (valor != 0):
    soma = soma + valor
    valor = int(input("Digite um Valor: "))
    contador = contador + 1

print("A soma dos valores é: " + str(soma))
print("A quantidade de valores é: " + str(contador))
