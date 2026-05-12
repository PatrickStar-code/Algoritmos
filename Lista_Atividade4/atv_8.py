numbers = [85,52,12,10,65,77,3.2]

if any(isinstance(item, float) for item in numbers):
    print("possui valores float")
else:
    print("não possui valores float")

