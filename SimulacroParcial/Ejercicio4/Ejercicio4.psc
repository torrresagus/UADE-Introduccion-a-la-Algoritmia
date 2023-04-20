Algoritmo Ejercicio4
	par = 0
	impar = 0
	Para i<-1 Hasta 50 Hacer
		Escribir "Ingrese un numero: "
		Leer numero
		Si numero mod 2 == 0 Entonces
			par = par + 1
		SiNo
			impar = impar + 1
		FinSi
		Si i == 1 Entonces
			maximo = numero
			minimo = numero
		SiNo
			Si maximo < numero Entonces
				maximo = numero
			SiNo
				Si minimo > numeo Entonces
					minimo = numero
				FinSi
			FinSi
		FinSi
	FinPara
	Escribir "El maximo ingresado: " , maximo
	Escribir "El minimo ingresado: " , minimo
	Escribir "Cantidad de Pares: ", par
	Escribir "Cantidad de Impares: ", impar
FinAlgoritmo
