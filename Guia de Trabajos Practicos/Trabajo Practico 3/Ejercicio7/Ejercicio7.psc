Algoritmo Ejercicio7
	Escribir "Ingrese un a�o: "
	Leer A�o
	Si A�o % 4 == 0 Entonces
		Si A�o % 100 == 0 Entonces
			Si A�o % 400 == 0 Entonces
				Escribir "El a�o es bisiesto"
			SiNo
				Escribir "El a�o no es bisiesto"
			FinSi
		SiNo
			Escribir "El a�o es bisiesto"
		FinSi
	SiNo
		Escribir "El a�o no es bisiesto"
	FinSi
FinAlgoritmo
