#Ejercicio 9: Un videojuego lleva registro del mejor puntaje indicando nombre y cantidad de puntos 
#obtenidos. Escribir un algoritmo que permita ingresar el nombre de cada jugador y su puntaje 
#obtenido. Para indicar que no hay más jugadores se ingresa la palabra “fin” como nombre. 
#¿Cuántos valores existen entre el menor y el mayor?

# Ingreso de datos
nombre = input("Ingrese el nombre del jugador: ")
puntaje = int(input("Ingrese el puntaje del jugador: "))
mayor = puntaje
menor = puntaje
cantidad = 0

while nombre != "fin":
    if puntaje > mayor:
        mayor = puntaje
    if puntaje < menor:
        menor = puntaje
    cantidad = cantidad + 1
    nombre = input("Ingrese el nombre del jugador: ")
    puntaje = int(input("Ingrese el puntaje del jugador: "))

if cantidad > 0:
    print("El mayor puntaje es:", mayor)
    print("El menor puntaje es:", menor)
    print("La cantidad de valores entre el menor y el mayor es:", mayor - menor - 1)

print("La cantidad de jugadores es:", cantidad)
