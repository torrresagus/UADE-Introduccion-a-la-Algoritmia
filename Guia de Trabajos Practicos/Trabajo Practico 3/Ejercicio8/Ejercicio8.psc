Algoritmo Ejercicio8
	Escribir "Ingrese un Dia: "
	Leer Dia
	Escribir "Ingrese un Mes: "
	Leer Mes
	Escribir "Ingrese un Año: "
	Leer Año	
	Si Mes >= 1 Y Mes <= 12 Entonces
		Si Mes == 2 Entonces
			Si Año % 4 == 0 Entonces
				Si Año % 100 == 0 Entonces
					Si Año % 400 == 0 Entonces
						Si Dia <= 29 Y Dia >= 1 Entonces
							Escribir "La fecha es Valida porque el año es Bisiesto"
						SiNo
							Escribir "La Fecha es Invalida"
						FinSi
					SiNo
						Si Dia <= 28 Y Dia >= 1 Entonces
							Escribir "La fecha es Valida"
						SiNo
							Escribir "La Fecha es Invalida"
						FinSi
					FinSi
				SiNo
					Si Dia <= 29 Y Dia >= 1 Entonces
						Escribir "La fecha es Valida, el año es Bisiesto"
					SiNo
						Escribir "La Fecha es Invalida"
					FinSi
				FinSi
			SiNo
				Si Dia <= 28 Y Dia >= 1 Entonces
					Escribir "La fecha es Valida"
				SiNo
					Escribir "La Fecha es Invalida"
				FinSi
			FinSi
		SiNo
			Si Mes == 1 O Mes == 3 O Mes == 5 O Mes == 7 O Mes == 8 O Mes == 10 O Mes == 12 Entonces
				Si Dia >= 1 Y Dia <= 31 Entonces
					Escribir "La fecha es Valida"
				SiNo
					Escribir "La Fecha es Invalida"
				FinSi
			SiNo
				Si Dia >= 1 Y Dia <= 30 Entonces
					Escribir "La fecha es Valida"
				SiNo
					Escribir "La Fecha es Invalida"
				FinSi
			FinSi
		FinSi
	SiNo
		Escribir "La Fecha Indicada no es Valida"
	FinSi
FinAlgoritmo
