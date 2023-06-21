#Desarrollar un programa que cree una matriz de 3x3 con valores al azar entre dos números ingresados por teclado.
#Verificar que el rango ingresado por el usuario sea válido, caso contrario solicitar nuevamente ambos valores. Calcular la
#suma de todos los elementos impares de la matriz, y luego, visualizarlo por pantalla.
#Nota: Utilizar cuatro funciones, la primera para el programa principal, la segunda para la carga de la matriz, la tercera para
#la suma de los números impares de la matriz y la última para la impresión de la matriz y suma de los elementos impares.
#Puede utilizar la RANDOM. Ejemplo:
#Matriz:
# 1 3 4 
# 6 2 9
# 2 5 7
#La suma de los números impares es: 25

import random

def cargarMatriz(n,m):
    
    a =  int(input("Ingrese el valor minimo del rango de valores Aleatorios: "))
    b = int(input("Ingrese el valor maximo del rango de valores Aleatorios: "))
    
    while a > b:
        print("El valor minimo no puede ser mas grande que el maximo: ")
        a =  int(input("Ingrese el valor minimo del rango de valores Aleatorios: "))
        b = int(input("Ingrese el valor maximo del rango de valores Aleatorios: "))

    Matriz = []
    for i in range(n):
        Matriz.append([])
        for j in range(m):
            Matriz[i].append(random.randint(a,b))
    
    return Matriz

def imprimirMatriz(matriz):
    print("Matriz: \n")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print("\n")


def sumaImpares(matriz):
    suma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] % 2 != 0:
                suma += matriz[i][j]
    return suma

def main():
    n = m = 3
    matrizCargada = cargarMatriz(n,m)
    imprimirMatriz(matrizCargada)
    suma = sumaImpares(matrizCargada)
    print(f"La suma de los numeros inmpares es {suma}")

main()