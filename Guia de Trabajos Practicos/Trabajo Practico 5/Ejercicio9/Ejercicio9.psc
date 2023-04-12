Algoritmo Ejercicio9
	Escribir 'Ingrese un Numero: '
	Leer numero
	Mientras numero<0 Hacer
		Escribir 'Ingrese un Numero Positivo: '
		Leer numero
	FinMientras
	suma <- 0
	Para i<-0 Hasta numero+1 Hacer
		Si i MOD 2<>0 Entonces
			suma <- suma+i
			Escribir (i)
		FinSi
	FinPara
	Escribir 'La suma de los números impares es: ',suma
FinAlgoritmo
