#Ejercicio 6: Leer un número entero y mostrar un mensaje informando cuántos dígitos contiene. 
#Tener en cuenta que el número puede ser negativo. 
#Ejemplo: Si se ingresa 12345 se debe imprimir 5.

numero = int(input("Ingrese un número entero: "))
if numero < 0:
    numero = numero * -1
digitos = 0
while numero > 0:
    numero = numero // 10
    digitos += 1
print("El número ingresado tiene", digitos, "dígitos")
