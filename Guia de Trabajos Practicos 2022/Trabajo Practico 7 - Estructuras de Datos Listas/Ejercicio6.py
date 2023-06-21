#Escribir una función para devolver una lista con todas las posiciones que ocupa 
#un valor pasado como parámetro, utilizando búsqueda secuencial en una lista 
#desordenada. La función debe devolver una lista vacía si el elemento no se encuentra en la lista original.

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
