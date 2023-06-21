#Rellenar una lista con números enteros entre 0 y 100 obtenidos al azar e imprimir el valor mínimo y el lugar que ocupa. Tener en cuenta que el mínimo puede 
#estar repetido, en cuyo caso deberán mostrarse todas las posiciones en las que 
#se encuentre. La carga de datos termina cuando se obtenga un 0 como número 
#al azar, el que no deberá cargarse en la lista.

import random

def minimo(lista):
    minimo = lista[0]
    for i in range(len(lista)):
        if lista[i] < minimo:
            minimo = lista[i]
    return minimo

def posiciones(lista, minimo):
    posiciones = []
    for i in range(len(lista)):
        if lista[i] == minimo:
            posiciones.append(i)
    return posiciones

def main():
    lista = []
    numero = random.randint(0, 100)
    while numero != 0:
        lista.append(numero)
        numero = random.randint(0, 100)
    print(lista)
    minimo = minimo(lista)
    print("El minimo es ", minimo)
    posiciones = posiciones(lista, minimo)
    print("Las posiciones son: ", posiciones)

main()
