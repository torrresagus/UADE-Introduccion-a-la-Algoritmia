#Crear una lista de N números generados al azar entre 0 y 100 pero sin elementos repetidos. El valor de N se ingresa por teclado. Resolver este problema utilizando dos estrategias distintas:
#· Impidiendo el agregado de elementos repetidos
#· Eliminando los duplicados luego de generar la lista. Asegurarse que la 
#cantidad final de elementos sea la solicitada

import random

#Primera estrategia

def lista_sin_repetidos1(tamaño):
    lista = []
    while len(lista) < tamaño:
        numero = random.randint(0, 100)
        if numero not in lista:
            lista.append(numero)
    return lista

#Segunda estrategia

def lista_sin_repetidos2(tamaño):
    lista = []
    while len(lista) < tamaño:
        numero = random.randint(0, 100)
        lista.append(numero)
    lista_sin_repetidos = []
    for i in range(len(lista)):
        if lista[i] not in lista_sin_repetidos:
            lista_sin_repetidos.append(lista[i])
    return lista_sin_repetidos

def main():
    tamaño = int(input("Ingrese el tamaño de la lista: "))
    lista = lista_sin_repetidos1(tamaño)
    print(lista)
    lista = lista_sin_repetidos2(tamaño)
    print(lista)

main()


