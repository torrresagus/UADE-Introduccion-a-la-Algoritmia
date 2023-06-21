#Dada una lista ordenada de números llamada A y un nuevo número N, desarrollar un programa que agregue el elemento N dentro de la lista A, respetando el 
#ordenamiento existente. El programa deberá detectar automáticamente si el ordenamiento es ascendente o descendente antes de realizar la inserción. No se 
#permite añadir el elemento al final y reordenar la lista. 

def ordenamiento(lista):
    if lista[0] < lista[1]:
        return "ascendente"
    else:
        return "descendente"
    
def agregar(lista, numero):
    if ordenamiento(lista) == "ascendente":
        for i in range(len(lista)):
            if lista[i] > numero:
                lista.a(i, numero)
                break
    else:
        for i in range(len(lista)):
            if lista[i] < numero:
                lista.insert(i, numero)
                break
    return lista

def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8]
    numero = int(input("Ingrese el numero a agregar: "))
    lista = agregar(lista, numero)
    print(lista)

main()
