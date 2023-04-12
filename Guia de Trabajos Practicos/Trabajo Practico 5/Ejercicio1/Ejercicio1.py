#Ejercicio 1:Leer números que representan edades de un grupo de personas, 
#finalizando la lectura cuando se ingrese el número -1. Imprimir cuántos son menores de 18 años, 
#cuántos tienen 18 años o más y el promedio de edad de ambos grupos. Descartar valores que no 
#representan una edad válida. (Se considera válida una edad entre 0 y 100).

sumaMenores = 0
sumaMayores = 0
cantMenores = 0
cantMayores = 0
edad = 0
while edad != -1:
    edad = int(input("Ingrese una edad: "))
    if edad >= 0 and edad <= 100:
        if edad < 18:
            sumaMenores += edad
            cantMenores += 1
        else:
            sumaMayores += edad
            cantMayores += 1
    else:
        print("Edad inválida")
promedioMenores = sumaMenores / cantMenores
promedioMayores = sumaMayores / cantMayores
print("Cantidad de menores de 18 años: ", cantMenores)
print("Cantidad de mayores de 18 años: ", cantMayores)
print("Promedio de edad de menores de 18 años: ", promedioMenores)
print("Promedio de edad de mayores de 18 años: ", promedioMayores)
