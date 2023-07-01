#Generar una matriz cuadrada de NxN. Informar cuál es la suma de los elementos
#ubicados en el triángulo superior de la misma.
import random

def cargarMatriz(n,m):
    matriz = []
    for i in range (n):
        matriz.append([])
        for j in range(m):
            matriz[i].append(random.randint(1,100))
    return matriz

def sumaTrianguloSuperior(matriz):
    suma = 0
    for i in range(len(matriz)):
        for j in range (len(matriz)):
            if(i < j):
                suma = suma + matriz[i][j]
    return suma
            
def imprimirMatriz(matriz):
    print("Matriz \n")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print("\n")


def main():
    n = m = 5
    matriz = cargarMatriz(n,m)  
    suma = sumaTrianguloSuperior(matriz)
    imprimirMatriz(matriz)
    print (suma)

main()