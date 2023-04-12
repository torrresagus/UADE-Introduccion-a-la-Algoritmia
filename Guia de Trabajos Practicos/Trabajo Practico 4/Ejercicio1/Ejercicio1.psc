Algoritmo Ejercicio1
	contador = 1
	Escribir "ingrese numeros enteros, para finalizar ingrese -1"
	Leer num
	Mientras num <> -1 Hacer
		Si contador = 1 Entonces
			primero = num
			contador <- 2
		FinSi
		ultimo <- num
		Leer num
	FinMientras
	Si contador = 2 Entonces
		Escribir "El primer numero es: ", primero
		Escribir "El ultimo numero es: ", ultimo
	SiNo
		Escribir "No ingreso un valor"
	FinSi
FinAlgoritmo
