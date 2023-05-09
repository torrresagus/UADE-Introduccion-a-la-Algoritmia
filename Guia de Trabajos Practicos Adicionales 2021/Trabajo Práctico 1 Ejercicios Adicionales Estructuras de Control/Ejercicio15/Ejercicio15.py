#Ejercicio 15: Diseñar una función para verificar si un número es par o impar, devolviendo True o False.}

def par(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
num = int(input("Ingrese un número: "))
if par(num):
    print("El número", num, "es par")
else:
    print("El número", num, "es impar")

    