#Calcular la suma de los números de la lista.

def sumar(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma

def cargar_lista(tamaño):
    lista = []
    for i in range(tamaño):
        numero = int(input(f"Ingrese el numero {i + 1}: "))
        lista.append(numero)

def main():
    tamaño = int(input("Ingrese el tamaño de la lista: "))
    lista = cargar_lista(tamaño)

    suma = sumar(lista)
    print("La suma de los numeros de la lista es: ", suma)

main()
