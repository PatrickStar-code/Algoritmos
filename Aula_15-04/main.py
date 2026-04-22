import time

numbers = [7,5,2,1,3,6]
target = 7

match = {}

inicio1 = time.time()

for i in numbers:
    if(target - i) in match:
        print(f"{ match[target - i][0]} + {i} = {target}")
    match[i] = [i, False]

fim1 = time.time()
print(f"Tempo: {fim1 - inicio1}")

inicio2 = time.time()

for i in numbers:
    for j in numbers:
        if(i + j == target):
            print(f"{i} + {j} = {target}")

fim2 = time.time()
print(f"Tempo: {fim2 - inicio2}")
