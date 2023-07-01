#Generar una matriz de MxN con valores al azar comprendidos entre A y B. Mostrar la suma de los valores ubicados sobre la diagonal principal. Los valores de A
#y B también se ingresan por teclado.

import random

def cargarMatriz(n,m):
    A = int(input("Ingrese el valor minimo que se debe elegir al azar: "))
    B = int(input("Ingrese el valor maximo que se debe elegir al azar: "))

    matriz = []

    for i in range(n):
        matriz.append([])
        for j in range(m):
            matriz[i].append(random.randint(A, B))

    return matriz

def sumaDiagonal(matriz):
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][i]

    return suma

#Para verificar el ejercico,imprimimos la matriz
def imprimirMatriz(matriz):
    print("Matriz \n")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print("\n")

def main():
    m = n = 5
    matriz = cargarMatriz(m,n)
    suma = sumaDiagonal(matriz)
    print(f"La suma de la diagonal princial de la matriz es: {suma} \n ")
    imprimirMatriz(matriz)

main()
