#Realizar un programa para ingresar desde el teclado un conjunto de números e 
#informar si la cantidad de elementos es impar o par, sin utilizar contadores. 
#Fi-nalizar la lectura de datos con -1

num = 0
impar = False
while num != -1:
    num = int(input("Ingrese un numero: "))
    if num != -1:
        impar = not impar

if impar:
    print("La cantidad de elementos es impar")
else:
    print("La cantidad de elementos es par")
