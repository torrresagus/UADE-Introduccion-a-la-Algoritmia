#Ejercicio 3:Desarrollar un programa que solicite un número de mes (por ejemplo 4) 
#y escriba el nombre del mes en letras ("abril"). Verificar que el mes sea válido y 
#mostrar un mensaje de error en caso de que no lo sea
NumeroMes = int(input("Ingresar un Numero de Mes: "))
if  NumeroMes < 1 or NumeroMes > 12:
    print("El numero", NumeroMes, " no es un mes valido!")
elif NumeroMes == 1:
    print("El mes", NumeroMes, " es Enero!")
elif NumeroMes == 2:
    print("El mes", NumeroMes, " es Febrero!")
elif NumeroMes == 3:
    print("El mes", NumeroMes, " es Marzo!")
elif NumeroMes == 4:
    print("El mes", NumeroMes, " es Abril!")
elif NumeroMes == 5:
    print("El mes", NumeroMes, " es Mayo!")
elif NumeroMes == 6:
    print("El mes", NumeroMes, " es Junio!")
elif NumeroMes == 7:
    print("El mes", NumeroMes, " es Julio!")
elif NumeroMes == 8:
    print("El mes", NumeroMes, " es Agosto!")
elif NumeroMes == 9:
    print("El mes", NumeroMes, " es Septiembre!")
elif NumeroMes == 10:
    print("El mes", NumeroMes, " es Octubre!")
elif NumeroMes == 11:
    print("El mes", NumeroMes, " es Noviembre!")
elif NumeroMes == 12:
    print("El mes", NumeroMes, " es Diciembre!")
else:
    print("El numero", NumeroMes, " no es un mes valido!")
        