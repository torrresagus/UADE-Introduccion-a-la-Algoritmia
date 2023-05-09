Algoritmo Ejercicio11
	Escribir 'Ingrese un numero natural: '
	Leer H
	primo <- Verdadero
	Para i<-2 Hasta H-1 Hacer
		Si H MOD i=0 Entonces
			primo <- Falso
		FinSi
	FinPara
	Si primo Entonces
		Escribir 'El numero ',H,' es primo'
	SiNo
		Escribir 'El numero ',H,' no es primo'
	FinSi
FinAlgoritmo
