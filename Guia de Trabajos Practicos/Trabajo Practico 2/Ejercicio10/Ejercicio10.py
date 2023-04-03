#Ejercicio 10:Leer un período en segundos e imprimirlo expresado en días, horas, minutos y segundos. 
#Por ejemplo, 200000 segundos equivalen a 2 días, 7 horas, 33 minutos y 20 segundos.
Segundos = int(input("Ingrese un periodo en segundos: "))
Dias = Segundos // 86400
#Re asigno el valor de Segundos para que no se acumule el resto de la division anterior
Segundos = Segundos % 86400
Horas = Segundos // 3600
#Re asigno el valor de Segundos para que no se acumule el resto de la division anterior
Segundos = Segundos % 3600
Minutos = Segundos // 60
#Re asigno el valor de Segundos para que no se acumule el resto de la division anterior
Segundos = Segundos % 60
print("El periodo ingresado equivale a: ", Dias, " dias, ", Horas, " horas, ", Minutos, " minutos y ", Segundos, " segundos.")