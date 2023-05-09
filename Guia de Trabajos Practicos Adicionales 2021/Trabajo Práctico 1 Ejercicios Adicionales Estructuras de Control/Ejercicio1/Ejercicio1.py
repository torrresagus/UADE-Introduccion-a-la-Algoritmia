#Ejercicio 1: Ingresar la edad de dos hermanos e indicar quién es el mayor o si son mellizos.

edad1 = int(input("Ingrese la edad del primer hermano: "))
edad2 = int(input("Ingrese la edad del segundo hermano: "))
if edad1 > edad2:
    print("El primer hermano es mayor")
elif edad1 < edad2:
    print("El segundo hermano es mayor")
else:
    print("Son mellizos")
