frase = input("Digite uma frase ")
frase.lower()

c = input("DIgite um caracter ")

for i in frase:
    if i == c:
        print(i)
        break
    