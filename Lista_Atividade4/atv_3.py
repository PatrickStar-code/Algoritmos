inteiros = [1,2,3,4,5,6,7,8,9,10]
maior = inteiros[0]
pos = 0

for i in inteiros:
    if i > maior:
        maior = i
        pos = inteiros.index(i)

print(maior,pos)

