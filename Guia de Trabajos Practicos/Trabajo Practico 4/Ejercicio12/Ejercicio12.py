#Ejercicio 12:La sucesión de Fibonacci es una sucesión de números enteros donde cada tér-mino 
#se obtiene como suma de los dos anteriores, siendo los dos primeros 0 y 1. 
#Por lo tanto, Fib=0, 1, 1, 2, 3, 5, 8, 13, 21.... Realizar un programa que lea N e imprima los N
# primeros términos de esta sucesión, como así también la suma de los mismos.

N = int(input("Ingrese un numero natural: "))
fib = 0
fib1 = 1
fib2 = 0
suma = 0
print("Los primeros ", N, " numeros de la sucesion de Fibonacci son: ")
for i in range(0, N):
    print(fib)
    suma += fib
    fib2 = fib1
    fib1 = fib
    fib = fib1 + fib2
print("La suma de los primeros ", N, " numeros de la sucesion de Fibonacci es: ", suma)

