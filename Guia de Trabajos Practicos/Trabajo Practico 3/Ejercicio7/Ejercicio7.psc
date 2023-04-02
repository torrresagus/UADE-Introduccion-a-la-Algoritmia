Algoritmo Ejercicio7
	Escribir "Ingrese un año: "
	Leer Año
	Si Año % 4 == 0 Entonces
		Si Año % 100 == 0 Entonces
			Si Año % 400 == 0 Entonces
				Escribir "El año es bisiesto"
			SiNo
				Escribir "El año no es bisiesto"
			FinSi
		SiNo
			Escribir "El año es bisiesto"
		FinSi
	SiNo
		Escribir "El año no es bisiesto"
	FinSi
FinAlgoritmo
