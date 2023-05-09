#Ejercicio 11:Un banco necesita para sus cajeros automáticos un programa que lea una cantidad de dinero 
#e imprima a cuántos billetes equivale, conside-rando que existen billetes de $1000, $500, $100, $50, $10, $5 y $1. 
#Desarrollar dicho programa de tal forma que se minimice la cantidad de billetes entregados por el cajero
Monto = int(input("Ingrese un monto: "))
Billetes1000 = Monto // 1000
#Re asigno el valor de Monto para que no se acumule el resto de la division anterior
Monto = Monto % 1000
Billetes500 = Monto // 500
#Re asigno el valor de Monto para que no se acumule el resto de la division anterior
Monto = Monto % 500
Billetes100 = Monto // 100
#Re asigno el valor de Monto para que no se acumule el resto de la division anterior
Monto = Monto % 100
Billetes50 = Monto // 50
#Re asigno el valor de Monto para que no se acumule el resto de la division anterior
Monto = Monto % 50
Billetes10 = Monto // 10
#Re asigno el valor de Monto para que no se acumule el resto de la division anterior
Monto = Monto % 10
Billetes5 = Monto // 5
#Re asigno el valor de Monto para que no se acumule el resto de la division anterior
Monto = Monto % 5
Billetes1 = Monto // 1
print("El monto ingresado equivale a: ", Billetes1000, " billetes de $1000, ", Billetes500, " billetes de $500, ", Billetes100, " billetes de $100, ", Billetes50, " billetes de $50, ", Billetes10, " billetes de $10, ", Billetes5, " billetes de $5 y ", Billetes1, " billetes de $1.")