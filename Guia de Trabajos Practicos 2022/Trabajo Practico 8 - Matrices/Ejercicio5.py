#Desarrollar una función para crear una matriz de MxN. La función recibe M y N
#por parámetro, la rellena con valores al azar entre A y B (también recibidos por
#parámetro) y retorna la matriz creada. Si no hay valores entre A y B o alguna de
#las dimensiones es negativa se deberá retornar la matriz vacía. Desarrollar también un pequeño programa principal para invocar a la función y mostrar la matriz
#por pantalla. Además mostrar la suma de cada fila y cada columna.

import random

def crearMatriz(m,n):
    a = int(input("Ingrese el valor minimo: "))
    b = int(input("Ingrese el valor maximo: "))

    matriz = []
    if a < b and m > 0 and n > 0:
        for i in range(m):
            matriz.append([])
            for j in range(n):
                matriz[i].append(random.randint(a,b))
    return matriz

def imprimirMatriz(matriz):
    print("Matriz \n")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print("\n")

def sumarFilas(matriz):
    suma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            suma += matriz[i][j]
        print(f"La suma de la fila {i + 1} es: {suma}")
        suma = 0

def sumarColumnas(matriz):
    suma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            suma += matriz[j][i]
        print(f"La suma de la columna {i + 1} es: {suma}")
        suma = 0

def main():
    m = int(input("Ingrese la cantidad de filas: "))
    n = int(input("Ingrese la cantidad de columnas: "))
    matriz = crearMatriz(m,n)
    imprimirMatriz(matriz)
    sumarFilas(matriz)
    sumarColumnas(matriz)

main()
