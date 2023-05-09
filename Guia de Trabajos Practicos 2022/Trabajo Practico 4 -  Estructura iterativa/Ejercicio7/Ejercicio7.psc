Algoritmo Ejercicio7
	suma <- 0
	mayor <- 0
	posicion <- 0
	Para i<-0 Hasta 9 Hacer
		Escribir 'Ingrese un numero: '
		Leer num
		suma <- suma+num
		Si num>mayor Entonces
			mayor <- num
			posicion <- i+1
		FinSi
	FinPara
	promedio <- suma/10
	Escribir 'El promedio de los numeros ingresados es: ',promedio
	Escribir 'El mayor numero ingresado es: ',mayor
	Escribir 'El mayor numero ingresado se encuentra en la posicion: ',posicion
FinAlgoritmo
