#Determinar si la lista es capicúa (palíndromo). Una lista capicúa se lee de igual 
#modo de izquierda a derecha y de derecha a izquierda. Por ejemplo, [2, 7, 7, 2] 
#es capicúa, mientras que [2, 7, 5, 2] no lo es.

def esCapicua(lista):
    capicua = True
    for i in range(len(lista) // 2):
        if lista[i] != lista[len(lista) - 1 - i]:
            print (lista[i], lista[len(lista) - 1 - i])
            capicua = False
            print("La lista no es capicua")
#            return False
#    return True
    return capicua

def cargarLista(tamaño):
    lista = []
    for i in range(tamaño):
        numero = int(input(f"Ingrese el numero {i + 1}: "))
        lista.append(numero)
    return lista


def main():
    tamaño = int(input("Ingrese el tamaño de la lista: "))
    lista = cargarLista(tamaño)
    if esCapicua(lista):
        print("La lista es capicua")
    else:
        print("La lista no es capicua")

main()

