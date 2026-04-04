valor = 0
intervalo0_25 = 0
intervalo26_50 = 0
intervalo51_75 = 0
intervalo76_100 = 0

while valor >= 0:
    valor = int(input("Digite um número (negativo para encerrar): "))
    if(valor >= 0 <= 25):
        print("Intervalo [0, 25]")
        intervalo0_25 += 1
    elif(valor >= 26 <= 50):
        print("Intervalo [26, 50]")
        intervalo26_50 += 1
    elif(valor >= 51 <= 75):
        print("Intervalo [51, 75]")
        intervalo51_75 += 1
    elif(valor >= 76 <= 100):
        print("Intervalo [76, 100]")
        intervalo76_100 += 1
    elif(valor < 0):
        print("Encerrando programa.")
    else:
        print("Valor fora dos intervalos definidos.")
        
print(f"Total de números no intervalo [0, 25]: {intervalo0_25}")
print(f"Total de números no intervalo [26, 50]: {intervalo26_50}")
print(f"Total de números no intervalo [51, 75]: {intervalo51_75}")
print(f"Total de números no intervalo [76, 100]: {intervalo76_100}")
  
 