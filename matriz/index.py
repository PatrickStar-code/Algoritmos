
import random


def criarMatriz(matrix,num_col,num_linha):
    for i in range(num_linha):
        linha = []
        for j in range(num_col):
            valor = random.randint(1,10)
            linha.append(valor)
        matrix.append(linha)
    return(matrix)

def printMatrix(matriz):
    for i in range(len(matriz)):
        print(f"Linha {i + 1} : {matriz[i]}")

def somarTodasaColuna(matriz,coluna):
    soma = 0
    for i in range(len(matriz)):
        soma=soma + matriz[i][0]
    print(f"soma coluna {coluna} igual a {soma}")

def somarDiagonal(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma +=matriz[i][i]
    print(f"soma Diagonal: {soma}")

def somarLinha(matriz,linha):
    soma = 0
    for i in range(len(matriz[linha])):
        soma += matriz[linha][i]
    print(soma)    
    

def somarDiagonalInvertida(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma +=matriz[i][len(matriz)-1-i]
    print(f"A soma secundaria é de {soma}")
            
numeros = []
matriz = criarMatriz(numeros,2,2)
printMatrix(matriz)
somarTodasaColuna(matriz=matriz,coluna=0)
somarDiagonal(matriz=matriz)
somarDiagonalInvertida(matriz=matriz)
somarLinha(matriz=matriz,linha=0)