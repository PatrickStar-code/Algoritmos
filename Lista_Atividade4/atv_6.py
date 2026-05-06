palavra = input("Digite uma palavra ")
n = int(input("Digite um numero "))

if(n >= palavra.__len__()):
    print(palavra)
else:
    for i in range(n):
        print(palavra[i])