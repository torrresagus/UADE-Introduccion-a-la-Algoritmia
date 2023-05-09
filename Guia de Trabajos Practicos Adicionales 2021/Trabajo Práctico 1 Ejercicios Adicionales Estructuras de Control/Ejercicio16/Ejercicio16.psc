Algoritmo Ejercicio16
	Escribir "Ingrese un numero: "
	Leer num
	suma = 0
	cantidad = 0
	Mientras num <> -1 Hacer
		Si num mod 2 == 0 Entonces
			cantidad = cantidad + 1
			suma = suma + num
		FinSi
		Escribir "Ingrese un numero: "
		Leer num
	FinMientras
	Escribir "La cantidad de numeros pares ingresados es: " , cantidad
	Escribir "La suma de los numeros pares ingresados es: " , suma
FinAlgoritmo
