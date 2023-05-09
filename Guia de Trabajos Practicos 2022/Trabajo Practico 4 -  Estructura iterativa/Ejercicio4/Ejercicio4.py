#Ejercicio 4:Desarrollar un programa que imprima la suma de los números impares compren-didos entre 42 y 176.

suma = 0
for i in range(42, 176):
    if i % 2 != 0:
        suma += i

print("La suma de los numeros impares entre 42 y 176 es: ", suma)