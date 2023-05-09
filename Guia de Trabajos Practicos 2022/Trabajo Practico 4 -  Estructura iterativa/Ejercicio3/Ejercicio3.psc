Algoritmo Ejercicio3
	num <- 0
	mayor <- 0
	menor <- 0
	Mientras num<>-1 Hacer
		Escribir 'Ingrese un numero: '
		Leer num
		Si num<>-1 Entonces
			Si num>mayor Entonces
				mayor <- num
			FinSi
			Si num<menor O menor=0 Entonces
				menor <- num
			FinSi
		FinSi
	FinMientras
	Escribir 'El mayor numero ingresado es: ',mayor
	Escribir 'El menor numero ingresado es: ',menor
FinAlgoritmo
