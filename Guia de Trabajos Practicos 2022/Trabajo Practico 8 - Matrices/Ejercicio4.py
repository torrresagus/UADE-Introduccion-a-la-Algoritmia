#Indicar las coordenadas del mayor valor encontrado en una matriz de MxN, 
#generada con valores aleatorios entre 100 y 1000.

import random

def cargarMatriz(n,m):
    matriz = []
    for i in range(n):
        matriz.append([])
        for j in range(m):
            matriz[i].append(random.randint(100,1000))
    return matriz

def mayorElemento(matriz):
    mayor = []

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if len(mayor) == 0:
                mayor.append(i)
                mayor.append(j)
            elif matriz[mayor[0]][mayor[1]] < matriz[i][j]:
                mayor[0] = i
                mayor[1] = j

    return mayor

#Para verificar el ejercico,imprimimos la matriz
def imprimirMatriz(matriz):
    print("Matriz \n")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print("\n")

def main():
    n = 5
    m = 5
    matriz = cargarMatriz(n,m)

    imprimirMatriz(matriz)

    mayor = mayorElemento(matriz)

    print(f"El mayor elemento esta en las cordenadas: {mayor}")

main()