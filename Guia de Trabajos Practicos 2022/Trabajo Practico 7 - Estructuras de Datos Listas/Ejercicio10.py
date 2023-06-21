#Eliminar de una lista de números enteros los valores que se encuentren en una 
#segunda lista. Imprimir la lista original, la lista de valores a eliminar y la lista 
#resultante. Ambas listas deben rellenarse con números al azar. La cantidad y el 
#rango de los valores los decide el programador. 

import  random

def eliminar(lista1, lista2):
    for i in range(len(lista2)):
        if lista2[i] in lista1:
            lista1.remove(lista2[i])
    return lista1

def generar_lista(tamaño):
    lista = []
    for i in range(tamaño):
        numero = random.randint(0, 100)
        lista.append(numero)
    return lista



def main():
    lista1 = []
    lista2 = []
    tamaño1 = int(input("Ingrese el tamaño de la primera lista: "))
    tamaño2 = int(input("Ingrese el tamaño de la segunda lista: "))
    lista1 = generar_lista(tamaño1)
    lista2 = generar_lista(tamaño2)
    print("La primera lista es: ", lista1)
    print("La segunda lista es: ", lista2)
    lista1 = eliminar(lista1, lista2)
    print("La lista resultante es: ", lista1)

main()

