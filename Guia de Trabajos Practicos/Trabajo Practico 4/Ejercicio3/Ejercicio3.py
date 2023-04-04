#Ejercicio 3:Realizar un programa para ingresar desde el teclado un conjunto de números y 
#mostrar por pantalla el menor y el mayor de ellos. Finalizar la lectura de datos con un valor -1.

num = 0
mayor = 0
menor = 0

while num != -1:
    num = int(input("Ingrese un numero: "))
    if num != -1:
        if num > mayor:
            mayor = num
        if num < menor:
            menor = num

print("El mayor numero ingresado es: ", mayor)
print("El menor numero ingresado es: ", menor)
