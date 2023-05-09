#Realizar un programa para ingresar desde el teclado un conjunto de números. 
#Al finalizar mostrar por pantalla el primer y último valor ingresado. Finalizar la lec-tura con -1.
print("Ingrese numeros enteros, para finalizar ingrese -1")
num = int(input("Ingrese un numero: "))
primero = num
while num != -1:
    ultimo = num
    num = int(input("Ingrese un numero: "))
print("El primer numero ingresado es: ", primero)
print("El ultimo numero ingresado es: ", ultimo)
