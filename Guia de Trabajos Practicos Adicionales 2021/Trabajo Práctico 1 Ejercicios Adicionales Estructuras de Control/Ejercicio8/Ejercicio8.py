#Ejercicio 8: Se desea ingresar la nota de N alumnos y mostrar su promedio

# Ingreso de datos
cantidad = int(input("Ingrese la cantidad de alumnos: "))
suma = 0
for i in range(cantidad):
    nota = int(input("Ingrese la nota del alumno: "))
    suma = suma + nota
promedio = suma / cantidad
print("El promedio de las notas es: ", promedio)

