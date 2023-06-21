#Escribir una función para contar cuántas veces aparece un valor dentro de la 
#lista. La función recibe como parámetros la lista y el valor a buscar, y devuelve 
#un número entero.

def contar(lista, valor):
    contador = 0
    for i in range(len(lista)):
        if lista[i] == valor:
            contador += 1
    return contador

def main():
    tamaño = int(input("Ingrese el tamaño de la lista: "))
    lista = []
    for i in range(tamaño):
        numero = int(input(f"Ingrese el numero {i + 1}: "))
        lista.append(numero)
    valor = int(input("Ingrese el valor a buscar: "))
    contador = contar(lista, valor)
    print("El valor aparece ", contador, " veces en la lista")

main()
