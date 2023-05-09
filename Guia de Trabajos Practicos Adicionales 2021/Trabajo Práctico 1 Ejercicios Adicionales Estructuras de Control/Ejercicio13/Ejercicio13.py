#Ejercicio 13: Diseñar una función que reciba un nombre como parámetro y lo salude por pantalla. Por 
#ejemplo, si recibe el dato “Juan”, debe mostrar: “Hola Juan”.

def saludar(nombre):
    print("Hola", nombre)

nombre = input("Ingrese su nombre: ")
saludar(nombre)
