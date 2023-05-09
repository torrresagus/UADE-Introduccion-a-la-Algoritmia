Algoritmo Ejercicio2
	num <- 0
	impar <- Falso
	Mientras num<>-1 Hacer
		Escribir 'Ingrese un numero: '
		Leer num
		Si num<>-1 Entonces
			impar <- NO impar
		FinSi
	FinMientras
	Si impar Entonces
		Escribir 'La cantidad de elementos es impar'
	SiNo
		Escribir 'La cantidad de elementos es par'
	FinSi
FinAlgoritmo
