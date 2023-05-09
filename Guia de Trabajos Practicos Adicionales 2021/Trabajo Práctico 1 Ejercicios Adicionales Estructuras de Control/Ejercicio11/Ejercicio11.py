#Ejercicio 11: Escribir un algoritmo que calcule la raíz cuadrada del número que introduzca el usuario. Si se 
#introduce un número negativo, debe mostrar un mensaje de error y volver a pedirlo (tantas 
#veces como sea necesario)

# Ingreso de datos
numero = int(input("Ingrese un número: "))
while numero < 0:
    print("Error, el número debe ser positivo")
    numero = int(input("Ingrese un número: "))
    
raiz = numero ** 0.5

print("La raíz cuadrada del número ingresado es:", raiz)

