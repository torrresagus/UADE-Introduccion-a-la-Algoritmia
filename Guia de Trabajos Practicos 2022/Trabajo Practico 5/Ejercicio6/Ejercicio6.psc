Algoritmo Ejercicio6
	Escribir 'Ingrese un n�mero entero: '
	Leer numero
	Si numero<0 Entonces
		numero <- numero*(-1)
	FinSi
	digitos <- 0
	Mientras numero>0 Hacer
		numero <- trunc(numero / 10)
		digitos <- digitos+1
	FinMientras
	Escribir 'El n�mero ingresado tiene ',digitos,' d�gitos'
FinAlgoritmo
