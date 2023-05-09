#Ejercicio 11:Realizar un programa que lea un número natural H e imprima un mensaje 
#indi-cando si H es primo o no. Se dice que un número es primo cuando sólo es divi-sible 
#por sí mismo y por la unidad.

H = int(input("Ingrese un numero natural: "))
primo = True
for i in range(2, H):
    if H % i == 0:
        primo = False
        break

if primo:
    print("El numero ", H, " es primo")
else:
    print("El numero ", H, " no es primo")
