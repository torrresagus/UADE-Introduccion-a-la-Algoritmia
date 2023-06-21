#Crear una matriz cuadrada y luego generar una lista que contenga la suma de cada una de las filas de la matriz. Mostrar la matriz con los datos de la carga en formato de matriz y la lista con los resultados obtenidos. Ejemplo:

#Matriz:     
#1   13   4
#16  2    9
#2   5   17

#Lista:
#18 27 24


#Nota: debe utilizar funciones para el programa principal, la carga de la matriz, la generación de la lista y la impresión de la matriz y lista. Puede utilizar la librería RANDOM en la función de carga de la matriz. Ingresar valores del 1 al 100. 

import random

def cargar_matriz(n, m):
    matriz = []
  
    for i in range(n):
        matriz.append([])
        for j in range(m):
            matriz[i].append(random.randint(1, 100))
    return matriz

def calcular_lista(matriz):
    suma_lista = []
    acumulador = 0
  
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            acumulador += matriz[i][j]
        suma_lista.append(acumulador)
        acumulador = 0
    return suma_lista

def imprimir(matriz_cargada, suma_lista):
    print("Matriz: \n")
    for i in range(len(matriz_cargada)):
        for j in range(len(matriz_cargada[i])):
            print(matriz_cargada[i][j], end=" ")
        print("\n")
      
    print("Lista: \n")
    for i in range(len(suma_lista)):
        print(suma_lista[i], end=" ")

def main():
    m = n = int(input("Ingrese dimensión: "))
    matriz_cargada = cargar_matriz(n, m)
    suma_lista = calcular_lista(matriz_cargada)
    imprimir(matriz_cargada, suma_lista)

main()
