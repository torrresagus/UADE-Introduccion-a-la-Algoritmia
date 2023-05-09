Algoritmo Ejercicio7
	Escribir "Ingrese un número entero: "
	Leer numero
	Si numero < 0 Entonces
		numero <- numero * (-1)
		negativo <- Verdadero
	Sino
		negativo <- Falso
	Fin Si
	numero_invertido <- 0
	Mientras numero > 0 Hacer
		numero_invertido <- numero_invertido * 10 + numero Mod 10
		numero <- trunc(numero / 10)
	Fin Mientras
	Si negativo Entonces
		numero_invertido <- numero_invertido * (-1)
	Fin Si
	Escribir "El número invertido es: ", numero_invertido
FinAlgoritmo
