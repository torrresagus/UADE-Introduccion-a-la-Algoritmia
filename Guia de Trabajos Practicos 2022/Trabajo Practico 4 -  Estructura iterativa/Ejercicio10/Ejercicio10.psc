Algoritmo Ejercicio10
	Escribir "Ingrese un numero: "
	Leer num
	factorial <- 1
	Si num < 0 Entonces
		Escribir "El numero ingresado es invalido"
	Sino
		Para i <- 1 Hasta num Con Paso 1 Hacer
			factorial <- factorial * i
		Fin Para
		Escribir "El factorial de ", num, " es: ", factorial
	Fin Si
	
FinAlgoritmo
