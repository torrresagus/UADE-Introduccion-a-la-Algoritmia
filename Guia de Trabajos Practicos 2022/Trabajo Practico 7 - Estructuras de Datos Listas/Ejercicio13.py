#Leer dos listas de números M y N y ordenarlas de menor a mayor. Luego se solicita generar e imprimir una tercera lista que resulte de intercalar los elementos 
#de M y N. La nueva lista también debe quedar ordenada, sin utilizar ningún método de ordenamiento en ella

import random

def cargar_lista(tamaño):
    lista = []
    for i in range(tamaño):
        numero = random.randint(1, 100)
        lista.append(numero)
    return lista

def ordenar(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] < lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
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
    lista1 = ordenar(lista1)
    lista2 = ordenar(lista2)
    print("La primera lista ordenada es: ", lista1)
    print("La segunda lista ordenada es: ", lista2)
    lista3 = intercalar(lista1, lista2)
    print("La lista intercalada es: ", lista3)

main()
