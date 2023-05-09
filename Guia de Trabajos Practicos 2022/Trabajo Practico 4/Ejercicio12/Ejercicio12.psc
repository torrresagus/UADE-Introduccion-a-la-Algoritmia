Algoritmo Ejercicio12
	Escribir 'Ingrese un numero natural: '
	Leer N
	fib <- 0
	fib1 <- 1
	fib2 <- 0
	suma <- 0
	Escribir 'Los primeros ',N,' numeros de la sucesion de Fibonacci son: '
	Para i<-0 Hasta N-1 Hacer
		Escribir fib
		suma <- suma+fib
		fib2 <- fib1
		fib1 <- fib
		fib <- fib1+fib2
	FinPara
	Escribir 'La suma de los primeros ',N,' numeros de la sucesion de Fibonacci es: ',suma
FinAlgoritmo
