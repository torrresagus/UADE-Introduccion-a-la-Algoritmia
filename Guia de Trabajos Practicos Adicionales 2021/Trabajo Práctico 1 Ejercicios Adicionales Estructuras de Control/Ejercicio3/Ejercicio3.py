#Ejercicio 3: Ingresar los nombres de dos visitantes al Parque de Diversiones y sus respectivas edades y 
#alturas. Decidir quién/es pueden acceder a una montaña rusa cuyo uso requiere tener una 
#edad mínima de 15 años y una altura superior a 1,5m.

nombre1 = input("Ingrese el nombre del primer visitante: ")
edad1 = int(input("Ingrese la edad del primer visitante: "))
altura1 = float(input("Ingrese la altura del primer visitante: "))
nombre2 = input("Ingrese el nombre del segundo visitante: ")
edad2 = int(input("Ingrese la edad del segundo visitante: "))
altura2 = float(input("Ingrese la altura del segundo visitante: "))

if edad1 >= 15 and altura1 > 1.5:
    if edad2 >= 15 and altura2 > 1.5:
        print(nombre1 + " y " + nombre2 + " pueden acceder a la montaña rusa")
    else:
        print(nombre1 + " puede acceder a la montaña rusa")
else:
    if edad2 >= 15 and altura2 > 1.5:
        print(nombre2 + " puede acceder a la montaña rusa")
    else:
        print("Ninguno de los dos puede acceder a la montaña rusa")
