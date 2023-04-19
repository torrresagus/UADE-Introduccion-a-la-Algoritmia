Algoritmo SimulacroParcial
	Escribir "Ingrese el numero del dado al tirarlo"
	Leer resultadoDado
	Si resultadoDado >= 1 Y resultadoDado <= 6 Entonces
		Si resultadoDado == 1 Entonces
			Escribir "La cara opuesta de ", resultadoDado, "es SEIS"
		SiNo
			Si resultadoDado == 2 Entonces
				Escribir "La cara opuesta de ", resultadoDado, "es CINCO"
			SiNo
				Si resultadoDado == 3 Entonces
					Escribir "La cara opuesta de ", resultadoDado, "es CUATRO"
				SiNo
					Si resultadoDado == 4 Entonces
						Escribir "La cara opuesta de ", resultadoDado, "es TRES"
					SiNo
						Si resultadoDado == 5 Entonces
							Escribir "La cara opuesta de ", resultadoDado, "es DOS"
						SiNo
							Escribir "La cara opuesta de ", resultadoDado, "es UNO"
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
	SiNo
		Escribir "ERROR: numero incorrecto"
	FinSi
FinAlgoritmo
