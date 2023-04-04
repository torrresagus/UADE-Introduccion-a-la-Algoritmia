#Ejercicio 8:Ingresar números, hasta que la suma de los números pares supere 100. 
#Mostrar cuántos números se ingresaron en total.
suma = 0
cantidad = 0
while suma <= 100:
    numero = int(input("Ingrese un numero: "))
    if numero % 2 == 0:
        suma += numero
    cantidad += 1
print("La suma de los numeros pares ingresados es: ", suma)
print("La cantidad de numeros pares ingresados es: ", cantidad)
