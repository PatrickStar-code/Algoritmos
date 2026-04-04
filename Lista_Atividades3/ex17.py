numeroPerfeitoEncontrados = 0
numeroAtual = 1
while numeroPerfeitoEncontrados < 3:
    somaDivisores = 0
    for i in range(1, numeroAtual):
        if numeroAtual % i == 0:
            somaDivisores += i
    if somaDivisores == numeroAtual:
        print(f"{numeroAtual} é um número perfeito.")
        numeroPerfeitoEncontrados += 1
    numeroAtual += 1

