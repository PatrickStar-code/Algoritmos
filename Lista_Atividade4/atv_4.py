inteiros = [89,46,25,16,10,5,2,1]
organizado = []


for i in inteiros:
    for j in inteiros:
        if i > j:
            j = i
    organizado.insert(0,j)


print(organizado)