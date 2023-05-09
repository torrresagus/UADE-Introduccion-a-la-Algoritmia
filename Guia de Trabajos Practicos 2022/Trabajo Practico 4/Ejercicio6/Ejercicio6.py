#Ejercicio 6:Mostrar la tabla de multiplicar (entre 1 y 12) del número 4. 
#¿Cómo cambiaría el algoritmo para que el usuario pueda decidir la tabla de multiplicar a mostrar?

print("La tabla de multiplicar del 4 es: ")
for i in range(1, 13):
    print("4 * ", i, " = ", 4 * i)

#En caso de que el usuario quiera ver la tabla de multiplicar de otro numero, se le pedira que ingrese el numero
#y se mostrara la tabla de multiplicar de ese numero
numero = int(input("Ingrese el numero del cual quiere ver la tabla de multiplicar: "))
print("La tabla de multiplicar del ", numero ,"es: ")
for i in range(1, 13):
    print(numero," * ", i, " = ", numero * i)
