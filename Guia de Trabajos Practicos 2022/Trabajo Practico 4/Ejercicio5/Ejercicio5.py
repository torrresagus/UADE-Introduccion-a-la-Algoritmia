#Ejercicio 5:Desarrollar un programa que imprima los números naturales comprendidos entre 1 y N. 
#El valor de N se ingresa desde el teclado.

n = int(input("Ingrese un numero: "))
print("Los numeros naturales comprendidos entre 1 y ", n, " son: ")
for i in range(1, n + 1):
    print(i)