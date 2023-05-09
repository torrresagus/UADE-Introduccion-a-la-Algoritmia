#Ejercicio 14: Diseñar una función que devuelva el máximo entre dos números recibidos como parámetros.

def maximo(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
    
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
print("El máximo entre", num1, "y", num2, "es", maximo(num1, num2))

