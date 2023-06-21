#Ejercicio 7: Ídem anterior, utilizando búsqueda binaria sobre una lista ordenada.


def buscar(lista, valor):
    posiciones = []
    for i in range(len(lista)):
        if lista[i] == valor:
            posiciones.append(i)
    return posiciones

def main():
    tamaño = int(input("Ingrese el tamaño de la lista: "))
    lista = []
    for i in range(tamaño):
        numero = int(input(f"Ingrese el numero {i + 1}: "))
        lista.append(numero)
    valor = int(input("Ingrese el valor a buscar: "))
    posiciones = buscar(lista, valor)
    print("El valor aparece en las posiciones: ", posiciones)

main()
