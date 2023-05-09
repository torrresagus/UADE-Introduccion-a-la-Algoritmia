#Ejercicio 16: Ingresar números hasta ingresar -1. Informar cuántos números pares se ingresaron y su suma.

# Ingreso de datos
numero = int(input("Ingrese un número: "))
cantidad = 0
suma = 0

while numero != -1:
    if numero % 2 == 0:
        cantidad = cantidad + 1
        suma = suma + numero
    numero = int(input("Ingrese un número: "))
 
print("La cantidad de números pares ingresados es:", cantidad)
print("La suma de los números pares ingresados es:", suma)
