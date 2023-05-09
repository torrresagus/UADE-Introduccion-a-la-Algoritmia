#Ejercicio 2: Ingresar la edad de una persona e indicar si es mayor de edad (mayor o igual a 18 años). 
#Utilizar una variable de tipo booleana para guardar el valor Verdadero si la persona tiene 18 
#años o más y Falso en caso contrario.

edad = int(input("Ingrese la edad de la persona: "))
if edad >= 18:
    mayor = True
else:
    mayor = False

if mayor:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

    
