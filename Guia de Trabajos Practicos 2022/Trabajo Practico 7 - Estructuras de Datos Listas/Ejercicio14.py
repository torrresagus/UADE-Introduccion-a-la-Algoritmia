# Una escuela necesita conocer cuántos alumnos cumplen años en cada mes del 
# año, con el propósito de ofrecerles un agasajo especial en su día. Desarrollar un 
# programa que lea el número de legajo y fecha de nacimiento (día, mes y año) de 
# cada uno de los alumnos que concurren a dicha escuela. La carga finaliza con un 
# número de legajo igual a -1. Emitir un informe donde aparezca -mes por mescuántos alumnos cumplen años a lo largo del año. Imprimir también una leyenda 
# que indique cuál es el mes con mayor cantidad de cumpleaños

import random

def cargar_lista(tamaño):
    lista = []
    for i in range(tamaño):
        numero = random.randint(1, 12)
        lista.append(numero)
    return lista

def contar(lista):
    lista2 = []
    for i in range(len(lista)):
        lista2.append(lista.count(lista[i]))
    return lista2

def main():
    tamaño = int(input("Ingrese el tamaño de la lista: "))
    lista = cargar_lista(tamaño)
    print("La lista es: ", lista)
    lista2 = contar(lista)
    print("La lista con la cantidad de cumpleaños por mes es: ", lista2)
    print("El mes con mayor cantidad de cumpleaños es: ", max(lista2))

main()
