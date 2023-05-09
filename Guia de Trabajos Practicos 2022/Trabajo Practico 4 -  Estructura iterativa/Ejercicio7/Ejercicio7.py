#Ejercicio 7:Leer 10 números enteros e imprimir su promedio, el mayor valor leído y 
#en qué posición se encontraba. Si se ingresó más de una vez sólo debe informar la pri-mera.

numeros = []
for i in range(10):
    numeros.append(int(input("Ingrese un numero: ")))

promedio = sum(numeros) / len(numeros)
mayor = max(numeros)
posicion = numeros.index(mayor) + 1

print("El promedio de los numeros ingresados es: ", promedio)
print("El mayor numero ingresado es: ", mayor)
print("El mayor numero ingresado se encuentra en la posicion: ", posicion)

#En caso de no poder utilizar las funciones MAX o LEN se puede hacer lo siguiente:
numero = int(input("Ingrese un numero: "))
mayor = numero
posicion = 1
suma = numero
for i in range(2, 11):
    numero = int(input("Ingrese un numero: "))
    suma += numero
    if numero > mayor:
        mayor = numero
        posicion = i

promedio = suma / 10

print("El promedio de los numeros ingresados es: ", promedio)
print("El mayor numero ingresado es: ", mayor)
print("El mayor numero ingresado se encuentra en la posicion: ", posicion)
