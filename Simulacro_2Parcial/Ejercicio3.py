# Queremos guardar los legajos y nombres de los empleados de una empresa y luego consultar si un legajo ingresado por el usuario existe en la nómina. Realiza un programa que introduzca el legajo y nombre de cada empleado. EI proceso de lectura de datos terminará cuando se introduzca como legajo un -1. Luego, introducir un legajo a buscar. Al finalizar se deberán mostrar los legajos y nombres de todos los emplea40s, ordenados por legajo (de menor a mayor) y la leyenda si el legajo está en la nómina de empleados. Ejemplo:
# EI número de legajo de Juan es 3.
# EI número de legajo de Marta es 7.
# EI número de legajo de Pedro es 15.
# En el caso que exista el legajo en la nómina: "EI legajo 15 está en la nómina."
# En el caso que NO exista el legajo en la nómina: "EI legajo 18 no está en la nómina."
# Nota: debe utilizar funciones para el programa principal, para la carga de las listas, para ordenar las listas, para la búsqueda
# binaria y para mostrar los datos. Para el ordenamiento, puede utilizar el método de burbujeo, selección o inserción, no
# puede utilizar la función SORT.

def cargarListas():
    legajos = []
    nombres = []
    legajo = int(input("Ingrese el legajo: "))
    while legajo != -1:
        nombre = input("Ingrese el nombre: ")
        legajos.append(legajo)
        nombres.append(nombre)
        legajo = int(input("Ingrese el legajo: "))
    return legajos, nombres

def ordenar_burbujeo(legajos, nombres):
    length = len(legajos)
    for i in range(length-1):
        for j in range(length-1):
            if legajos[j] > legajos[j+1]:
                aux = legajos[j]
                legajos[j] = legajos[j+1]
                legajos[j+1] = aux
                aux = nombres[j]
                nombres[j] = nombres[j+1]
                nombres[j+1] = aux
    return legajos, nombres

def binary_search(lista, valor):
    index_low = 0
    index_max = len(lista) - 1

    while index_low <= index_max:
        index_middle = (index_low + index_max) // 2
        if valor == lista[index_middle]:
            return True
        elif valor > lista[index_middle]:
            index_low = index_middle + 1
        else:
            index_max = index_middle - 1
    return False

def imprimirListas(legajos_ordenados, nombres_ordenados):
    for i in range(len(legajos_ordenados)):
        print(f"El número de legajo de {nombres_ordenados[i]} es {legajos_ordenados[i]}")

def main():
    legajos, nombres = cargarListas()
    legajo_buscar = int(input("Ingrese el legajo a buscar: "))
    legajos_ordenados, nombres_ordenados = ordenar_burbujeo(legajos, nombres)
    imprimirListas(legajos_ordenados, nombres_ordenados)
    if binary_search(legajos_ordenados, legajo_buscar):
        print(f"El legajo {legajo_buscar} está en la nómina.")
    else:
        print(f"El legajo {legajo_buscar} no está en la nómina.")

main()
