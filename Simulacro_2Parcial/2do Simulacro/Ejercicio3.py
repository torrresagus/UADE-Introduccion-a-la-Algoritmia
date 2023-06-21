#Ejercicio 3 (Puntaje: 40%)
#Desarrollar un algoritmo que permita crear al azar 5 números pertenecientes a la lista A y otros 5 números pertenecientes
#a la lista B. Crear una lista C, donde cada posición es eI resultado de la suma del número en la misma posición en la lisú A
#con eI número en la misma posición en la lista B. Finalmente, se ordena la lista C, de menor a mayor. Ejemplo: Se crea A
#(1, 2, 3,4, 51 y B (4, 7, 1, 3, 61 C: (5, 9, 4, 7, 111 y lista C ordenada (4, S, 7, 9, 11).
#Nota: Utilizar cinco funciones, la primera para el programa principal, la segunda para la carga de la lista (desde el programa
#principal se llama dos veces a la misma función para cargar A y B), la tercera para calcular la suma de las listas (C), la cuarta
#para el ordenamiento (burbujeo, selección o inserción) (C Ordenada) y la quinta para la impresión de todas las listas (A, B,
#C y C ordenada). Puede utilizar la librería RANDOM. Puede utilizar el método LIST o COPY.


import random
def imprimirLista(A, B, C, C_ordenada):
    print("La lista A: ", A)
    print("La lista B: ", B)
    print("La lista C: ", C)
    print("La lista C ordenada: ", C_ordenada)

def sumarListas(A, B):
    lista_sumada = []
    for i in range(len(A)):
        lista_sumada.append(A[i] + B[i])
    return lista_sumada

def cargarLista():
    lista = []
    for i in range(5):
        valor = random.randint(1, 10)
        lista.append(valor)
    return lista

def ordenarLista(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-1):
            if (lista[j] > lista[j + 1]):
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
    return lista

def main():
    A = cargarLista()
    B = cargarLista()
    C_original = sumarListas(A, B)
    C_copiada = C_original.copy() # desordenada
    lista_ordenada = ordenarLista(C_copiada)
    imprimirLista(A, B, C_original, lista_ordenada)

main()

