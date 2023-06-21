#Desarrollar una función que reciba la lista como parámetro y devuelva una nueva 
#lista con los mismos elementos de la primera, pero en orden inverso. Por 
#ejemplo, si la función recibe [5, 7, 1] debe devolver [1, 7, 5]

def invertir(lista):
    lista_invertida = []
    for i in range(len(lista) - 1, -1, -1):
        lista_invertida.append(lista[i])
    return lista_invertida

def main():
    tamaño = int(input("Ingrese el tamaño de la lista: "))
    lista = []
    for i in range(tamaño):
        numero = int(input(f"Ingrese el numero {i + 1}: "))
        lista.append(numero)
    lista_invertida = invertir(lista)
    print(f"La lista invertida es: {lista_invertida}")

main()
