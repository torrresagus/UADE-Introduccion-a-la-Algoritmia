#Cargar dos listas de números A y B con N números al azar entre 1 y 100, donde 
#N se ingresa por teclado. Mostrar ambas listas por pantalla. Luego construir e 
#imprimir tres nuevas listas C, D y E que contengan:
#· La concatenación de los valores pares de A con los impares de B. (valores pares o valores impares se refiere a los elementos propiamente dichos y no a sus posiciones).
#· La concatenación de los valores impares de A con el reverso de los valores pares de B. 
#· La intercalación de los elementos de A y B.

import random

def cargar_lista(tamaño):
    lista = []
    for i in range(tamaño):
        numero = random.randint(1, 100)
        lista.append(numero)
    return lista

def concatenar(lista1, lista2):
    lista = []
    for i in range(len(lista1)):
        if lista1[i] % 2 == 0:
            lista.append(lista1[i])
    for i in range(len(lista2)):
        if lista2[i] % 2 != 0:
            lista.append(lista2[i])
    return lista

def concatenar_inverso(lista1, lista2):
    lista = []
    for i in range(len(lista1)):
        if lista1[i] % 2 != 0:
            lista.append(lista1[i])
    for i in range(len(lista2)):
        if lista2[i] % 2 == 0:
            lista.append(lista2[i])
    return lista

def intercalar(lista1, lista2):
    lista = []
    if len(lista1) > len(lista2):
        for i in range(len(lista2)):
            lista.append(lista1[i])
            lista.append(lista2[i])
        for i in range(len(lista2), len(lista1)):
            lista.append(lista1[i])
    else:
        for i in range(len(lista1)):
            lista.append(lista1[i])
            lista.append(lista2[i])
        for i in range(len(lista1), len(lista2)):
            lista.append(lista2[i])
    return lista

def main():
    tamaño = int(input("Ingrese el tamaño de las listas: "))
    lista1 = cargar_lista(tamaño)
    lista2 = cargar_lista(tamaño)
    print("La primera lista es: ", lista1)
    print("La segunda lista es: ", lista2)
    lista3 = concatenar(lista1, lista2)
    print("La lista concatenada es: ", lista3)
    lista4 = concatenar_inverso(lista1, lista2)
    print("La lista concatenada con inverso es: ", lista4)
    lista5 = intercalar(lista1, lista2)
    print("La lista intercalada es: ", lista5)

main()
