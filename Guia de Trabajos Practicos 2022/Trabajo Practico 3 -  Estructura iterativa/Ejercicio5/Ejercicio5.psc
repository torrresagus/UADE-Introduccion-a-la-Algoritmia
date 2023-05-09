Algoritmo Ejercicio5
	CostoFinal = 0
	CostoBasico = 500
	CostoPorPagina = 3.20
	AgregadoTela = 200
	AgregadoEspecial = 336
	Escribir "Ingresar Cantidad de Paginas:"
	Leer Paginas
	CostoFInal = CostoBasico + CostoPorPagina * Paginas
	Si Paginas > 300 Entonces
		CostoFinal = CostoFinal + AgregadoTela
		Si Paginas > 600 Entonces
			CostoFinal = CostoFinal + AgregadoEspecial
			Escribir "El costo del libro con ", Paginas, " paginas tiene un costo de ", CostoFInal
		SiNo
			Escribir "El costo del libro con ", Paginas, " paginas tiene un costo de ", CostoFInal
		FinSi
	SiNo
		Escribir "El costo del libro con ", Paginas, " paginas tiene un costo de ", CostoFInal
	FinSi
FinAlgoritmo
