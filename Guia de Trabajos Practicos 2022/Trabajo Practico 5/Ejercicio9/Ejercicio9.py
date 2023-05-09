#Ejercicio 9: Ingresar un número N y validar que sea positivo. Luego:
#a. Mostrar los primeros números impares, hasta alcanzar el número ingresado.
#b. Informar la suma de esos números impares.
#Ejemplo:
#· Si se ingresa 5, se debe mostrar 1 3 5 y la suma es 9.
#· Si se ingresa 8, se debe mostrar 1 3 5 7 y la suma es 16.
#· Si se ingresa -5, se debe pedir otro número.

numero = int(input("Ingrese un numero: "))
while numero < 0:
    numero = int(input("Ingrese un numero positivo: "))
suma = 0
for i in range(numero + 1):
    if i % 2 != 0:
        suma += i
        print(i)
print("La suma de los numeros impares es: ", suma)