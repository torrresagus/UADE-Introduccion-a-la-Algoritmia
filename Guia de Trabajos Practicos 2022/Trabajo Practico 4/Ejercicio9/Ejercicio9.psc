Algoritmo Ejercicio9
	par <- 0
	impar <- 0
	patente <- 0
	Mientras patente<>-1 Hacer
		Escribir 'Ingrese la terminacion de la patente: '
		Leer patente
		Si patente>9 O patente<-1 Entonces
			Escribir 'La patente ingresada es invalida'
		SiNo
			Si patente<>-1 Entonces
				Si patente MOD 2=0 Entonces
					par <- par+1
				SiNo
					impar <- impar+1
				FinSi
			FinSi
		FinSi
	FinMientras
	Escribir 'La cantidad de patentes pares es: ',par
	Escribir 'La cantidad de patentes impares es: ',impar
FinAlgoritmo
