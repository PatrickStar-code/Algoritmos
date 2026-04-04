foraDoIntervalo = 0
dentroDoIntervalo = 0
for i in range(10):
    valor = float(input("Digite um valor: "))
    if 10<valor<20:
        print("Valor entre 10 e 20")
        dentroDoIntervalo += 1
    else:        
        print("Valor fora do intervalo")
        foraDoIntervalo += 1
print(f"Quantidade de valores dentro do intervalo: {dentroDoIntervalo}")
print(f"Quantidade de valores fora do intervalo: {foraDoIntervalo}")
