Algoritmo Ejercicio8
	suma <- 0
	cantidad <- 0
	Mientras suma<=100 Hacer
		Escribir 'Ingrese un numero: '
		Leer numero
		Si numero MOD 2=0 Entonces
			suma <- suma+numero
		FinSi
		cantidad <- cantidad+1
	FinMientras
	Escribir 'La suma de los numeros pares ingresados es: ',suma
	Escribir 'La cantidad de numeros pares ingresados es: ',cantidad
FinAlgoritmo
