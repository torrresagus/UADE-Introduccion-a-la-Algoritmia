#Ejercicio 7: Leer un número entero e invertir las cifras que contiene. 
#Imprimir por pantalla el número invertido. Tener en cuenta que el número puede ser negativo. 
#Por ejemplo, si se ingresa 1234 debe mostrar 4321.

numero = int(input("Ingrese un número entero: "))
if numero < 0:
    numero = numero * -1
    negativo = True
else:
    negativo = False
numero_invertido = 0
while numero > 0:
    numero_invertido = numero_invertido * 10 + numero % 10
    numero = numero // 10
if negativo:
    numero_invertido = numero_invertido * -1
print("El número invertido es:", numero_invertido)
