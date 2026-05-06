numeros = [25,12,-8,56,17,9,-3,42.56,2]
maior = numeros[0]
indice = 0

for numero in numeros:
    if numero > maior:
        maior = numero
        indice = numeros.index(numero)

print(maior)
print(indice)