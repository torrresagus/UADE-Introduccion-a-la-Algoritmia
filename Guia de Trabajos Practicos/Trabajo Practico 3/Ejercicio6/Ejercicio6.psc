Algoritmo Ejercicio6
	CostoFinal = 0
	CostoMinimo = 250
	CostoHasta10km = 30
	CostoMas10km = 20
	Escribir "Ingresar Cantidad de Kilometros:"
	Leer Kilometros
	Si Kilometros > 0 Entonces
		Si Kilometros > 10 Entonces
			CostoFinal = Kilometros * CostoMas10km
			Escribir "El costo por un viaje de ", Kilometros, " Km tes de ", CostoFinal
		SiNo
			Si (Kilometros * CostoHasta10km) > 250 Entonces
				CostoFinal = Kilometros * CostoHasta10km
				Escribir "El costo por un viaje de ", Kilometros, " Km es de ", CostoFinal
			SiNo
				CostoFinal = CostoMinimo
				Escribir "El costo por un viaje de ", Kilometros, " Km es de ", CostoFinal
			FinSi
		FinSi
	SiNo
		Escribir "Ingreso un numero incorrecto"
	FinSi
FinAlgoritmo
