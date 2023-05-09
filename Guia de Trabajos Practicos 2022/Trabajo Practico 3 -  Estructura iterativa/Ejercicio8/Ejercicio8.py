#Ejercicio 8:Leer tres números correspondientes al día, mes y año de una fecha e imprimir 
#un mensaje indicando si la fecha es válida o no
#Un año es bisiesto cuando es divisible por 4.
#Sin embargo, aquellos años que sean divisibles por 4 y también por 100 no son bisiestos,
#a menos que también sean divisibles por 400. Por ejemplo, 1900 no fue bisiesto pero sí el 2000.

Dia = int(input("Ingresar un Dia: "))
Mes = int(input("Ingresar un Mes: "))
Año = int(input("Ingresar un Año: "))
if Mes >= 1 & Mes <= 12:
    if Mes == 2:
        if Año % 4 == 0:
            if Año % 100 == 0:
                if Año % 400 == 0:
                    if Dia >= 1 & Dia <= 29:
                        print("La fecha", Dia, Mes, Año, " es valida!")
                    else:
                        print("La fecha", Dia, Mes, Año, " no es valida!")
                else:
                    if Dia >= 1 & Dia <= 28:
                        print("La fecha", Dia, Mes, Año, " es valida!")
                    else:
                        print("La fecha", Dia, Mes, Año, " no es valida!")
            else:
                if Dia >= 1 & Dia <= 29:
                    print("La fecha", Dia, Mes, Año, " es valida!")
                else:
                    print("La fecha", Dia, Mes, Año, " no es valida!")
        else:
            if Dia >= 1 & Dia <= 28:
                print("La fecha", Dia, Mes, Año, " es valida!")
            else:
                print("La fecha", Dia, Mes, Año, " no es valida!")
    elif Mes == 4 or Mes == 6 or Mes == 9 or Mes == 11:
        if Dia >= 1 & Dia <= 30:
            print("La fecha", Dia, Mes, Año, " es valida!")
        else:
            print("La fecha", Dia, Mes, Año, " no es valida!")
    elif Mes == 1 or Mes == 3 or Mes == 5 or Mes == 7 or Mes == 8 or Mes == 10 or Mes == 12:
        if Dia >= 1 & Dia <= 31:
            print("La fecha", Dia, Mes, Año, " es valida!")
        else:
            print("La fecha", Dia, Mes, Año, " no es valida!")
else:
    print("La fecha", Dia, Mes, Año, " no es valida!")

