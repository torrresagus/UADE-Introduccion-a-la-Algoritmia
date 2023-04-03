Algoritmo Ejercicio10
	Escribir 'Ingrese un periodo en segundos: '
	Leer Segundos
	Dias <- trunc(Segundos / 86400)
	Segundos <- Segundos MOD 86400
	Horas <- trunc(Segundos / 3600)
	Segundos <- Segundos MOD 3600
	Minutos <- trunc(Segundos/60)
	Segundos <- Segundos MOD 60
	Escribir 'El periodo ingresado equivale a: ',Dias,'Dias, ',Horas,'Horas, ',Minutos,'Minutos y ',Segundos,'Segundos.'
FinAlgoritmo
