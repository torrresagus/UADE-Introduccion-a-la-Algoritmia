#Crear una matriz de 3x4 (3 filas y 4 columnas) con valores obtenidos al azar 
#entre 1 y 10. Mostrar la matriz por pantalla respetando el formato de 3 filas y 4 
#columnas.

import random

def cargarMatriz(n,m):
    matriz = []
    for i in range(n):
        matriz.append([])
        for j in range(m):
            matriz[i].append(random.randint(1,10))
    
    return matriz

def imprimirMatriz(matriz):
    print("Matriz \n")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print("\n")

def main():
    matriz = cargarMatriz(3,4)
    imprimirMatriz(matriz)

main()