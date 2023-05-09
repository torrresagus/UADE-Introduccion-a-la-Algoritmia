#Ejercicio 4:Ingresar las notas de los dos parciales de un alumno e indicar si promocionó, 
#aprobó o si debe recuperar. Informar un error si el valor de alguna nota no está 
#entre 0 y 10.
#Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
#Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
#Se debe recuperar cuando al menos una de las dos notas es menor a 4.
Nota1 = float(input("Ingresar la Nota del Primer Parcial: "))
if Nota1 > 1 or Nota1 <= 10:
    Nota2 = float(input("Ingresar la Nota del Segundo Parcial: "))
    if Nota2 > 1 or Nota2 <= 10:
        if Nota1 >= 7 and Nota2 >= 7:
            print("El alumno promociono!")
        elif Nota1 >= 4 and Nota2 >= 4:
            print("El alumno aprobo!")
        else:
            print("El alumno debe recuperar!")
    else:
        print("La nota", Nota2, " no es valida!")
else:
    print("La nota", Nota1, " no es valida!")