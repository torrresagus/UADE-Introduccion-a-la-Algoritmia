#Ejercicio 7:Leer un número correspondiente a un año e imprimir un mensaje indicando si es bisiesto o no. 
#Un año es bisiesto cuando es divisible por 4. 
#Sin embargo, aquellos años que sean divisibles por 4 y también por 100 no son bisiestos, 
#a menos que también sean divisibles por 400. Por ejemplo, 1900 no fue bisiesto pero sí el 2000.
Año = int(input("Ingresar un Año: "))
if Año % 4 == 0:
    if Año % 100 == 0:
        if Año % 400 == 0:
            print("El año", Año, " es bisiesto!")
        else:
            print("El año", Año, " no es bisiesto!")
    else:
        print("El año", Año, " es bisiesto!")
else:
    print("El año", Año, " no es bisiesto!")
    