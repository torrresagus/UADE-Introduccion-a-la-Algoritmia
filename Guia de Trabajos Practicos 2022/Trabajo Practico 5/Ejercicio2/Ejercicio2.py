#Ejercicio 2:Escribir un programa que permita ingresar los números de legajo de los 
#alumnos de un curso y su nota de examen final. El fin de la carga se determina ingresan-do 
#un -1 en el legajo. Informar para cada alumno si aprobó o no el examen con-siderando que se
#aprueba con nota mayor o igual a 4. Se debe validar que la nota ingresada sea entre 1 y 10. 
#Terminada la carga de datos, informar:∑Cantidad de alumnos que aprobaron con nota mayor o igual a 4.
#Cantidad de alumnos que desaprobaron el examen con nota menor a 4.
#Porcentaje de alumnos que están aplazados (tienen 1 en el examen)

nota = 0
cantAprobados = 0
cantDesaprobados = 0
cantAplazados = 0
legajo = 0
while legajo != -1:
    legajo = int(input("Ingrese un legajo: "))
    if legajo != -1:
        nota = int(input("Ingrese una nota: "))
        if nota >= 1 and nota <= 10:
            if nota >= 4:
                cantAprobados += 1
            else:
                cantDesaprobados += 1
                if nota == 1:
                    cantAplazados += 1
        else:
            print("Nota inválida")
            
print("Cantidad de alumnos que aprobaron: ", cantAprobados)
print("Cantidad de alumnos que desaprobaron: ", cantDesaprobados)
print("Porcentaje de alumnos que están aplazados: ", cantAplazados / cantDesaprobados * 100, "%")
