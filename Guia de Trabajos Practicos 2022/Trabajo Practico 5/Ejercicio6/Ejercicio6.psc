Algoritmo Ejercicio6
	Escribir 'Ingrese un número entero: '
	Leer numero
	Si numero<0 Entonces
		numero <- numero*(-1)
	FinSi
	digitos <- 0
	Mientras numero>0 Hacer
		numero <- trunc(numero / 10)
		digitos <- digitos+1
	FinMientras
	Escribir 'El número ingresado tiene ',digitos,' dígitos'
FinAlgoritmo
