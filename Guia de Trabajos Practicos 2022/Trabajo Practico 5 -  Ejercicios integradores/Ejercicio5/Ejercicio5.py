#Ejercicio 5:Leer tres números D, M y A correspondientes al día, mes y año de una fecha, 
#y un número entero N que representa una cantidad de días. Realizar un programa que imprima 
#la nueva fecha que resulta de sumar N días a la fecha dada. Tener en cuenta los años bisiestos 
#tal como se detalla en el ejercicio 7 de la práctica 3.

D = int(input("Ingrese el día: "))
M = int(input("Ingrese el mes: "))
A = int(input("Ingrese el año: "))

N = int(input("Ingrese el número de días a sumar: "))

dias_mes_no_bisiesto = [31,28,31,30,31,30,31,31,30,31,30,31]
dias_mes_bisiesto = [31,29,31,30,31,30,31,31,30,31,30,31]

if A % 4 == 0 and A % 100 != 0 or A % 400 == 0:
    dias_mes = dias_mes_bisiesto
else:
    dias_mes = dias_mes_no_bisiesto

for i in range(N):
    D += 1
    if D > dias_mes[M-1]:
        D = 1
        M += 1
        if M > 12:
            M = 1
            A += 1
        if A % 4 == 0 and A % 100 != 0 or A % 400 == 0:
            dias_mes = dias_mes_bisiesto
        else:
            dias_mes = dias_mes_no_bisiesto

print("La nueva fecha es: ", D, "/", M, "/", A)
