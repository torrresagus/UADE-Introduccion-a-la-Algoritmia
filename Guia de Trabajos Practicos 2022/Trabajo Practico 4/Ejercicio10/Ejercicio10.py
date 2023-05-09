#Ejercicio 10:El factorial de un número entero N mayor que cero se define 
#como el producto de todos los enteros X tales que 0 < X <= N. Desarrollar 
#un programa para cal-cular el factorial de un número dado. Deberán rechazarse 
#las entradas inválidas (menores que 0).

num = int(input("Ingrese un numero: "))
factorial = 1
if num < 0:
    print("El numero ingresado es invalido")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("El factorial de ", num, " es: ", factorial)
