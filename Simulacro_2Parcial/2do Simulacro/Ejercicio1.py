#Escriba una función que tome una lista de números y devuelva la suma acumulada, es decir, una nueva lista donde el
#primer elemento es el mismo, el segundo elemento es la suma del primero con el segundo, el tercer elemento es la suma
#del resultado anterior con el siguiente elemento y así sucesivamente. Por ejemplo, la suma acumulada de (I, 2, 3) es (I,
#3, 61.

#Nota: EI ingreso de los números deben ser por teclado y finaliza cuando se ingresa el -1. Se deben utilizar mínimo cuatro
#funciones ara el ro rama rinci al ara la car a de la lista ara el cálculo de la suma acumulada en la nueva lista y


def cargarLista():
    numero = int(input("Ingrese numero para agregar a a lista: "))
    lista = []
    while numero != -1:
        lista.append(numero)
        numero = int(input("Ingrese numero para agregar a a lista: "))
    return lista

def sumar(lista):
    listaNueva = []
    suma = 0
    for i in range (len(lista)):
        suma += lista[i]
        listaNueva.append(suma)
    return listaNueva

def main():
    listaCargada = cargarLista()
    nuevaLista = sumar(listaCargada)
    print(listaCargada)
    print(nuevaLista)
main()
